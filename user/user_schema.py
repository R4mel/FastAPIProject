from fastapi import HTTPException
from pydantic import BaseModel, EmailStr, field_validator


class NewUserForm(BaseModel):
    email: EmailStr
    name: str
    phone: str
    password: str

    @field_validator('email', 'name', 'phone', 'password')
    def check_empty(cls, v):
        if not v or v.isspace():
            raise HTTPException(status_code=422, detail="필수 항목을 입력해주세요.")
        return v

    @field_validator('phone')
    def check_phone(cls, v):
        phone = v
        if '-' not in v or len(phone) != 13:
            raise HTTPException(status_code=422, detail="올바른 형식의 번호를 입력해주세요.")
        return phone

    @field_validator('password')
    def validate_password(cls, v):
        if len(v) < 8:
            raise HTTPException(status_code=422, detail="비밀번호는 8자리 이상 영문과 숫자를 포함하여 작성해 주세요.")

        if not any(char.isdigit() for char in v):
            raise HTTPException(status_code=422, detail="비밀번호는 8자리 이상 영문과 숫자를 포함하여 작성해 주세요.")

        if not any(char.isalpha() for char in v):
            raise HTTPException(status_code=422, detail="비밀번호는 8자리 이상 영문과 숫자를 포함하여 작성해 주세요.")

        return v


"""
1. email, name, phone, pw를 모두 빠짐없이 받아야 한다.

2. email이 email 형식이어야 한다.

3. phone의 형식은 000-0000-0000 이어야 한다.

4. 비밀번호는 8자 이상 영문과 숫자를 포함해야 한다.
"""
