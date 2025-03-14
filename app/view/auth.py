from fastapi import Depends
from fastapi.routing import APIRouter
from app.controller import AuthController
from app.dependency import DB
from app.model.validation import User
auth = APIRouter()

@auth.post('/signup')
def signup(user: User, db: DB)->str:
    """Signup Handler. Calls AuthController.signup and return token [str] on success"""
    return AuthController(db).signup(user.email, user.password)

    
    
@auth.post('/login')
def login(user: User, db: DB)->str:
    """Login Handler. Calls AuthController.login, returns token on success"""
    return AuthController(db).login(user.email, user.password)