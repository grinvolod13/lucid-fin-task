from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, sessionmaker
from app.const import CONFIG

engine_string = CONFIG['engine_string']
engine = create_engine(engine_string) # type: ignore
session_factory = sessionmaker(bind=engine)


def get_db():
    db = session_factory()
    try:
        yield db
        db.commit()
    except SQLAlchemyError as e:
        print("Error in session")
        db.rollback()
        raise e
    finally:
        db.close()
        
from fastapi import Depends
from typing import Annotated


DB = Annotated[Session, Depends(get_db)]