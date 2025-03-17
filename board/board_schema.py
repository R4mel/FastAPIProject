from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Pydantic의 BaseModel을 상속받아 정의
# Pydantic: 데이터 검증과 설정을 도와주는 라이브러리
# FastAPI 엔드포인트로 전달되는 JSON 데이터의 구조를 정의하고,
# 데이터가 올바른 타입과 형식을 갖추었는지 검증하는 데 사용
class NewPost(BaseModel):
  writer: str
  title: str
  content: Optional[str] = None


class PostList(BaseModel):
  no: int
  writer: str
  title: str
  date: datetime


class Post(BaseModel):
  no: int
  writer: str
  title: str
  content: Optional[str] = None
  date: datetime


class UpdatePost(BaseModel):
  no: int
  title: str
  content: Optional[str] = None