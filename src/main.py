from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

import config
from lifecycle import boot, shutdown
from routers import v1_router


@asynccontextmanager
async def app_lifespan(app: FastAPI):
    ## On Startup
    await boot()
    yield
    ## On Shutdown
    await shutdown()


app = FastAPI(lifespan=app_lifespan, title="Madsoft Memes API", )
# NOTE: you might want to just render media files using Nginx
app.mount("/media", StaticFiles(directory="media"), name="media")
# app.include_router(v1_router, prefix="/api") # NOTE: this is better
app.include_router(v1_router, prefix="")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    uvicorn.run(app, host=config.HOST, port=config.PORT, reload=False)
