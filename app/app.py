from contextlib import asynccontextmanager
from typing import AsyncIterator
from fastapi import FastAPI
from app.view import auth
from app.view import post_api


from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    """Caching initialization"""
    FastAPICache.init(InMemoryBackend(), prefix="fastapi-cache")
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(auth)    # login and signup
app.include_router(post_api)# posts router