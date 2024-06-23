import asyncio
import math

from fastapi import HTTPException, UploadFile
from tortoise.exceptions import DoesNotExist

from data_classes import CreateMeme, Meme, PaginatedResponse
from .files import FileService
from models import MemeModel


class MemesService(object):
    @classmethod
    async def get_meme_or_404(cls, id: int):
        meme = await cls.get_by_id(id)
        if not meme:
            raise HTTPException(
                status_code=404,
                detail=f"Meme with id {id} was not found.",
            )
        return meme

    @classmethod
    async def get_by_id(cls, id: int):
        try:
            return await MemeModel.get(id=id)
        except DoesNotExist:
            return None

    @classmethod
    async def get_paginated(cls, page: int, per_page: int, filters: dict):
        queryset, count = await cls.get_queryset(
            offset=per_page * (page - 1), limit=per_page, filters=filters
        )
        return PaginatedResponse[Meme](
            data=[i.to_meme() for i in queryset],
            count=count,
            page=page,
            per_page=per_page,
            pages=math.ceil(count / per_page),
        )

    @classmethod
    async def get_queryset(cls, offset: int, limit: int, filters: dict):
        query = MemeModel.filter(**filters)
        queryset, count = await asyncio.gather(
            query.offset(offset).limit(limit), query.count()
        )
        return queryset, count

    @classmethod
    async def create(cls, payload: CreateMeme):
        return await MemeModel.create(**payload.model_dump())

    @classmethod
    async def detail(cls, obj: Meme):
        return obj

    @classmethod
    async def update(cls, obj: MemeModel, payload: Meme):
        obj.update_from_dict(payload.model_dump())
        await obj.save()
        return obj

    @classmethod
    async def delete(cls, obj: MemeModel):
        await obj.delete()
