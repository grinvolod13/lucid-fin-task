import uuid
from email_validator import EmailNotValidError
from fastapi import HTTPException
from app.controller.base import Base
from app.model.orm import User

class AuthController(Base):
    ...
    def signup(self, email: str, password: str)->str:
        user = self.db.query(User).filter(User.email == email).one_or_none()
        if user:
            raise HTTPException(403, detail='User exists')
        
        token = str(uuid.uuid4())
        user = User(
            email=email,
            password=password,
            token = token,
        )
        self.db.add(user)
        return token
        
        
        
    def login(self, email, password)->str:
        user = self.db.query(User).filter(User.email == email, User.password == password).one_or_none()
        if not user:
            raise HTTPException(401, detail='Invalid email or password')
        
        return user.token