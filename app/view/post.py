from typing import Annotated
from fastapi import Body, Depends, Query
from fastapi.routing import APIRouter

from app.dependency import DB
from app.security import token_check
from app.model.validation import AddPostRequest, GetPostsRequest, DeletePostRequest

from app.controller import PostController
from fastapi_cache.decorator import cache


post_api = APIRouter()


@post_api.post('/post', dependencies=[Depends(token_check)])
def write_post(payload: AddPostRequest, db: DB):
    PostController(db).write_post(payload.token, payload.text)
    return {'status': 'ok'}
    

@post_api.get('/post')
@cache(expire=300)
async def get_all_posts(db:DB, token = Query(Depends(token_check)))->list[str]:
    return PostController(db).get_all_posts(token)

    
@post_api.delete('/post', dependencies=[Depends(token_check)])
def delete_post(payload: DeletePostRequest, db: DB):
    PostController(db).delete_post(payload.token, payload.postID)
    return {'status': 'ok'}

