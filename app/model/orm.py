from sqlalchemy.types import String, BLOB
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column, DeclarativeBase
from app.dependency import engine
from app.const import POST_SIZE_BYTES

class Base(DeclarativeBase):
    ...

class Post(Base):
    __tablename__ = 'post'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped['User'] = relationship(back_populates='posts')
    text: Mapped[bytes] = mapped_column(BLOB(POST_SIZE_BYTES), default=''.encode())
    
class User(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True) 
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column(String(256)) # as test task, i am sure its okay to leave it unashed and unsalted :D
    token: Mapped[str] = mapped_column(String(256))
    
    posts: Mapped[list[Post]] = relationship(back_populates='user')
    
    
    
Base.metadata.create_all(engine)
    
    
    
    

