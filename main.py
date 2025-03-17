from fastapi import FastAPI

import models
from database import engine
from user import user_router

from board import board_router

models.Base.metadata.create_all(bind=engine)
# SQLAlchemy를 이용하여 데이터베이스 테이블을 생성하는 코드
# 이를 통해 SQLAlchemy에서 정의한 데이터베이스 모델들을 실제 데이터베이스에 반영할 수 있음.

# SQLAlchemy: 파이썬에서 데이터베이스 작업을 돕기 위한 ORM(Object Relational Mapping) 라이브러리
# 데이터베이스 테이블과 파이썬 클래스를 연결하여 쿼리를 직접 작성하지 않고 데이터베이스 작업을 수행 가능
# Spring에서 JPA와 비슷한 기능
app = FastAPI()

app.include_router(board_router.app, tags=["board"])
app.include_router(user_router.app, tags=["user"])


@app.get("/")
async def root():
    return {"message": "Hello World"}

# async = 비동기 함수, 여러 작업을 거의 동시에 실행할 수 있는 프로그램
# I/O 작업(네트워크 요청, 파일 읽기/쓰기) 에서 시간이 오래 걸리는 작업을 처리할 때 효율적이다.