from typing import Annotated
from fastapi import Body, Depends
from fastapi.exceptions import HTTPException
from app.dependency import DB
from app.model.orm import User
from app.model.validation import Token



def single_token_check(token: str, db: DB):
    """Check token as string. Needed as dependency for token as Query parameter"""
    user = db.query(User).filter(User.token==token).one_or_none()
    if user:
        return user.token
    
    raise HTTPException(401, detail='invalid or missing token')

def token_check(payload: Token,  db: DB):
    """Check token as field of payload. Needed as dependency for token in Body parameters"""
    user = db.query(User).filter(User.token==payload.token).one_or_none()
    if user:
        return user.token
    
    raise HTTPException(401, detail='invalid or missing token')
    