from fastapi import APIRouter

from .memes import memes_router

# v1_router = APIRouter(prefix="/v1")
v1_router = APIRouter(prefix="")
v1_router.include_router(memes_router, prefix="/memes", tags=("Memes",))
