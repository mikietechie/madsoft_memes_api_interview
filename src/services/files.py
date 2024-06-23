import time

from fastapi import UploadFile
import aiofiles
from minio import Minio

import config

client = Minio(
    endpoint=config.MINIO_ENDPOINT,
    access_key=config.MINIO_ACCESS_KEY,
    secret_key=config.MINIO_SECRET_KEY,
    secure=config.MINIO_SECURE,
)

if not client.bucket_exists(config.MINIO_BUCKET):
    client.make_bucket(config.MINIO_BUCKET)


class FileService(object):

    @classmethod
    def get_file_name(cls, file: UploadFile) -> str:
        return f"{time.time()}-{file.filename}"

    @classmethod
    async def save_file_locally(cls, file: UploadFile) -> str:
        print(file.filename)
        file_name = cls.get_file_name(file)
        async with aiofiles.open(f"./media/{file_name}", "wb") as out:
            contents = file.file.read()
            await out.write(contents)
            await out.flush()
            file.file.close()
        return f"{config.ADDRESS}/media/{file_name}"

    @classmethod
    async def upload_file(cls, file: UploadFile) -> str:
        # return await cls.save_file_locally(file)
        file_name = cls.get_file_name(file)
        result = client.put_object(
            bucket_name=config.MINIO_BUCKET,
            object_name=file_name,
            data=file.file,
            length=-1,
            part_size=10 * 1024 * 1024,
        )
        file.file.close()
        return f"{config.MINIO_ADDRESS}/{config.MINIO_BUCKET}/{file_name}"

    @classmethod
    async def delete_file(cls, file_url: str):
        # TODO
        pass
