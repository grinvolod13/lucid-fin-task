from fastapi import HTTPException
from app.controller.base import Base
from app.model.orm import User, Post

class PostController(Base):
    def write_post(self, token: str, text: str):
        """create new post if correct token"""
        user = self.db.query(User).filter(User.token == token).one_or_none()
        if not user:
            raise HTTPException(401, detail='Invalid or missing token')
        self.db.add(Post(user_id=user.id, text=text.encode()))
    
    def delete_post(self, token: str, post_id: int):
        """create new post if correct token and post of it's Owner user exists"""
        user = self.db.query(User).filter(User.token == token).one_or_none()
        if not user:
            raise HTTPException(401, detail='Invalid or missing token')
        post = self.db.query(Post).filter(
            Post.id==post_id,
            Post.user_id==user.id,
        ).one_or_none()
        if not post:
            raise HTTPException(404, detail='Post not exists')
        self.db.delete(post)
    
    def get_all_posts(self, token: str) -> list[str]:
        """Return list of posts"""
        user = self.db.query(User).filter(User.token == token).one_or_none()
        if not user:
            raise HTTPException(401, detail='Invalid or missing token')
        posts_bytes: list[Post] = self.db.query(Post).filter(Post.user_id == user.id).all()
        posts = [post.text.decode() for post in posts_bytes] # decode from bytes (we store text as BLOB bytes in db)
        return posts