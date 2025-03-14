from fastapi import Depends
from fastapi.routing import APIRouter
from app.controller import AuthController
from app.dependency import DB
from app.model.validation import User
auth = APIRouter()

@auth.post('/signup')
def signup(user: User, db: DB)->str:
    return AuthController(db).signup(user.email, user.password)
    ...
    
    
@auth.post('/login')
def login(user: User, db: DB)->str:
    return AuthController(db).login(user.email, user.password)