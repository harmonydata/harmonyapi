"""
MIT License

Copyright (c) 2023 Ulster University (https://www.ulster.ac.uk).
Project: Harmony (https://harmonydata.ac.uk)
Maintainer: Thomas Wood (https://fastdatascience.com)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import sys

sys.path.append("./harmony/src")

import asyncio
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

from harmony_api.core.settings import settings
from harmony_api.routers.health_check_router import router as health_check_router
from harmony_api.routers.info_router import router as info_router
from harmony_api.routers.text_router import router as text_router
from harmony_api.services.instruments_cache import InstrumentsCache
from harmony_api.scheduler import scheduler
from harmony_api.services.vectors_cache import VectorsCache

description = """
Documentation for Harmony API.

Harmony is a tool using AI which allows you to compare items from questionnaires and identify similar content.
You can try Harmony at <a href="https://harmonydata.ac.uk/app">harmonydata.ac.uk/harmony_api</a> and you can read our blog at <a href="https://harmonydata.ac.uk">harmonydata.ac.uk</a>.
"""


@asynccontextmanager
async def lifespan(_: FastAPI):
    scheduler.start()

    yield

app_fastapi = FastAPI(
    title=settings.APP_TITLE,
    description=description,
    version=settings.VERSION,
    lifespan=lifespan,
    docs_url="/docs",
    contact={
        "name": "Thomas Wood",
        "url": "https://fastdatascience.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/license/mit/",
    },
)

app_fastapi.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS["origins"],
    allow_credentials=settings.CORS["allow_credentials"],
    allow_methods=settings.CORS["allow_methods"],
    allow_headers=settings.CORS["allow_headers"],
)

# Add gzip middleware
app_fastapi.add_middleware(GZipMiddleware)

# Include routers
app_fastapi.include_router(health_check_router, tags=["Health Check"])
app_fastapi.include_router(text_router, tags=["Text"])
app_fastapi.include_router(info_router, tags=["Info"])


async def main():
    # Load cache
    print("INFO:\t  Loading cache...")
    InstrumentsCache()
    VectorsCache()

    server = uvicorn.Server(
        config=uvicorn.Config(
            app=app_fastapi,
            host=settings.SERVER_HOST,
            port=settings.PORT,
            reload=settings.RELOAD,
            workers=1,
            loop="asyncio",
        )
    )

    api = asyncio.create_task(server.serve())

    # Start FastAPI
    print("INFO:\t  Starting application...")
    await asyncio.wait([api])


if __name__ == "__main__":
    asyncio.run(main())
