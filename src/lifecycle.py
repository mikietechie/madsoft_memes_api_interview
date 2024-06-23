from pathlib import Path

from tortoise import Tortoise
from fastapi.logger import logger

import config

## Setup directories
logger.info("Setting up directories")
media_path = "./media"
Path(media_path).mkdir(parents=True, exist_ok=True)

async def boot():
    # Connect to Database and Run Migrations
    logger.info("Making database connection")
    await Tortoise.init(db_url=config.DB_URI, modules={"models": ["models"]})
    await Tortoise.generate_schemas()


async def shutdown():
    # Close Database Connections
    await Tortoise.close_connections()
