from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URL = "sqlite:///./fastapi.db"

# DB 커넥션 풀 생성
engine = create_engine(DB_URL, pool_size=50, connect_args={"check_same_thread": False})
# check_same_thread= False: 동일한 스레드를 사용하지 않도록 설정

# DB접속을 위한 클래스
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# autocommit= False: 세션이 자동으로 커밋하지 않도록 설정
# autoflush= False: 세션이 자동으로 플러시하지 않도록 설정(플러시: 변동 사항을 데이터베이스에 반영)

# Base 클래스는 DB 모델 구성할 때 사용
Base = declarative_base()

# FastAPI 애플리케이션에서 데이터베이스 세션을 생성하고 관리하는 함수
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
