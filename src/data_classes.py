from typing import Generic, TypeVar
from pydantic import BaseModel

BC = TypeVar("BC")


class CreateMeme(BaseModel):
    text: str
    picture: str | None = None


class Meme(CreateMeme):
    id: int | None = None


class PaginatedResponse(BaseModel, Generic[BC]):
    data: list[BC]
    page: int
    per_page: int
    count: int
    pages: int


class User(BaseModel):
    id: int
    username: str
    password: str | None = None
