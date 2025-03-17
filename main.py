from fastapi import FastAPI

import models
from database import engine
from user import user_router

from board import board_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(board_router.app, tags=["board"])
app.include_router(user_router.app, tags=["user"])


@app.get("/")
async def root():
    return {"message": "Hello World"}
