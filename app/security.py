from typing import Annotated
from fastapi import Body, Depends
from fastapi.exceptions import HTTPException
from app.dependency import DB
from app.model.orm import User
from app.model.validation import Token

def token_check(payload: Annotated[Token, Body(embed=True)],  db: DB):
    
    user = db.query(User).filter(User.token==payload.token).one_or_none()
    if user:
        return user.token
    
    raise HTTPException(401, detail='invalid or missing token')
    