from typing import Annotated
from fastapi import Body, Depends
from fastapi.routing import APIRouter

from app.security import token_check
from app.model.validation import AddPostRequest, GetPostsRequest, DeletePostRequest


post_api = APIRouter(dependencies=[Depends(token_check)])


@post_api.post('/post')
def write_post(payload: AddPostRequest):
    
    ...
    
@post_api.get('/post')
def get_all_posts(payload: GetPostsRequest):
    ...
    
@post_api.delete('/post/{postID}')
def delete_post(payload: DeletePostRequest):
    ...

