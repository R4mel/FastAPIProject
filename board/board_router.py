from sqlalchemy.orm import Session
from database import get_db

from fastapi import APIRouter, Depends

from board import board_crud, board_schema

# FastAPI에서 사용하는 라우터 객체
app = APIRouter(
    prefix="/board",
)

# 새로운 게시글을 생성하는 엔드포인트 정의
# 데이터베이스 세션을 get_db 함수를 통해 종속성 주입으로 받습니다.
# 이는 Session 타입입니다.
@app.post(path="/create", description="기본 게시판 - 게시글 생성")
async def create_new_post(new_post: board_schema.NewPost, db: Session = Depends(get_db)):
  return board_crud.insert_post(new_post, db)


@app.get(path="/read", description="기본 게시판 - 게시글 조회")
async def read_all_post(db: Session = Depends(get_db)):
  return board_crud.list_all_post(db)


@app.get(path="/read/{post_no}", description="기본 게시판 - 특정 게시글 상세 조회")
async def read_post(post_no: int, db: Session = Depends(get_db)):
  return board_crud.get_post(post_no, db)


@app.put(path="/update/{post_no}", description="기본 게시판 - 특정 게시글 수정")
async def update_post(update_post: board_schema.UpdatePost, db: Session = Depends(get_db)):
  return board_crud.update_post(update_post, db)


@app.patch(path="/delete/{post_no}", description="기본 게시판 - 특정 게시글 삭제")
async def delete_post_yn(post_no: int, db: Session = Depends(get_db)):
 return board_crud.alter_del_yn(post_no, db)


@app.delete(path="/delete/{post_no}", description="기본 게시판 - 특정 게시글 삭제")
async def delete_post(post_no: int, db: Session = Depends(get_db)):
  return board_crud.delete_post(post_no, db)