import time

# import boto3
# from boto3.s3.transfer import S3Transfer
from fastapi import UploadFile
import aiofiles
from slugify import slugify

import config

# credentials = {
#     "aws_access_key_id": config.AWS_ACCESS_KEY_ID,
#     "aws_secret_access_key": config.AWS_SECRET_ACCESS_KEY,
# }

# client = boto3.client("s3", config.AWS_REGION, **credentials)
# transfer = S3Transfer(client)


class FileService(object):
    @classmethod
    async def save_file_locally(cls, file: UploadFile) -> str:
        print(file.filename)
        file_name = f"{time.time()}-{file.filename}"
        async with aiofiles.open(f"./media/{file_name}", "wb") as out:
            contents = file.file.read()
            await out.write(contents)
            await out.flush()
            file.file.close()
        return f"{config.ADDRESS}/media/{file_name}"

    @classmethod
    async def upload_file(cls, file: UploadFile) -> str:
        """Please not that I cannot have an AWS Account from Russia as of June 2024"""
        return await cls.save_file_locally(file)
        """TODO: Use an async boto3 library if i do manage to find a stable one"""
        # transfer.upload_file(
        #     file, #"/tmp/myfile",
        #     config.AWS_BUCKET,
        #     config.AWS_KEY,
        #     extra_args={"ACL": "public-read"},
        # )
        # file_url = "%s/%s/%s" % (
        #     client.meta.endpoint_url,
        #     config.AWS_BUCKET,
        #     config.AWS_KEY,
        # )
        # return file_url

    @classmethod
    async def delete_file(cls, file_url: str):
        # TODO
        pass
