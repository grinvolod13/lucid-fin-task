from typing import Annotated
from fastapi import Body, Depends
from fastapi.exceptions import HTTPException
from app.dependency import DB
from app.model.orm import User
from app.model.validation import Token



def single_token_check(token: str, db: DB):
    user = db.query(User).filter(User.token==token).one_or_none()
    if user:
        return user.token
    
    raise HTTPException(401, detail='invalid or missing token')

def token_check(payload: Token,  db: DB):
    
    user = db.query(User).filter(User.token==payload.token).one_or_none()
    if user:
        return user.token
    
    raise HTTPException(401, detail='invalid or missing token')
    