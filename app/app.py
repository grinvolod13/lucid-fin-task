from fastapi import FastAPI
from app.view import auth
from app.view import post_api

app = FastAPI()

app.include_router(auth)
app.include_router(post_api)