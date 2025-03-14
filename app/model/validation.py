from pydantic import BaseModel, Field, field_validator
from email_validator import validate_email, EmailNotValidError

from app.const import POST_SIZE_BYTES

class Token(BaseModel):
    token: str
    
class GetPostsRequest(Token):
    ...
class AddPostRequest(Token):
    text: str = Field(max_length=POST_SIZE_BYTES) # Validation of size (max 1Mb)
    
class DeletePostRequest(Token):
    postID: int


class User(BaseModel):
    email: str
    password: str = Field(min_length=8)
    
    @field_validator('email', mode='after')  
    @classmethod
    def email_check(cls, email: str) -> str:
        proccessed = validate_email(email, check_deliverability=False)
        return proccessed.normalized

    
