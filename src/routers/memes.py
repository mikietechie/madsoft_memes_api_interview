from typing import Annotated

from fastapi import (
    APIRouter,
    Query,
    Path,
    HTTPException,
    status,
    UploadFile,
    Form,
    File,
    Depends,
)
from fastapi.logger import logger
from data_classes import Meme, CreateMeme, PaginatedResponse
from services.memes import MemesService
from services.files import FileService
from services.security import SecurityService

memes_router = APIRouter()


@memes_router.get(
    "",
    response_model=PaginatedResponse[Meme],
    status_code=status.HTTP_200_OK,
)
async def list_memes(
    per_page: Annotated[int, Query(title="Memes per page", gt=0)] = 10,
    page: Annotated[int, Query(title="Page Number", gt=0)] = 1,
):
    # return PaginatedResponse[Meme](count=100, data=[], page=1, pages=10, per_page=10)
    return await MemesService.get_paginated(page=page, per_page=per_page, filters={})


@memes_router.post(
    "",
    response_model=Meme,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(SecurityService.is_authenticated)],
)
async def create_meme(
    file: Annotated[UploadFile, File()],
    text: Annotated[str, Form()],
) -> Meme:
    if file.size > 1024 * 1024:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail="File too large. Please upload a file less than 1mb",
        )
    try:
        url = await FileService.upload_file(file)
    except Exception as e:
        logger.error(e.with_traceback(None))
        raise HTTPException(status_code=400, detail="Failed to save file")
    payload = CreateMeme(text=text, picture=url)
    return await MemesService.create(payload=payload)


@memes_router.get("/{id}", response_model=Meme, status_code=status.HTTP_200_OK)
async def detail_meme(id: Annotated[int, Path(title="Meme ID", gt=0)]):
    return await MemesService.detail(await MemesService.get_meme_or_404(id))


@memes_router.put(
    "/{id}",
    response_model=Meme,
    status_code=status.HTTP_202_ACCEPTED,
    dependencies=[Depends(SecurityService.is_authenticated)],
)
async def update_meme(id: Annotated[int, Path(title="Meme ID", gt=0)], payload: Meme):
    return await MemesService.update(
        obj=await MemesService.get_meme_or_404(id), payload=payload
    )


@memes_router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(SecurityService.is_authenticated)],
)
async def delete_meme(id: Annotated[int, Path(title="Meme ID", gt=0)]) -> None:
    await MemesService.delete(obj=await MemesService.get_meme_or_404(id))
