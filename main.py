import asyncio

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

from core.settings import settings
from routers.health_check_router import router as health_check_router
from routers.info_router import router as info_router
from routers.text_router import router as text_router
from services.scheduler import app as app_rocketry

description = """
Documentation for Harmony API.

Harmony is a tool using AI which allows you to compare items from questionnaires and identify similar content.
You can try Harmony at <a href="https://app.harmonydata.org">app.harmonydata.org</a> and you can read our blog at <a href="https://harmonydata.org/blog/">harmonydata.org/blog/</a>.
"""

app_fastapi = FastAPI(
    title=settings.APP_TITLE,
    description=description,
    version=settings.VERSION,
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


class Server(uvicorn.Server):
    """
    Custom uvicorn.Server
    Override signals and include Rocketry
    """

    def handle_exit(self, sig: int, frame):
        app_rocketry.session.shut_down()

        return super().handle_exit(sig, frame)


async def main():
    server = Server(
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
    scheduler = asyncio.create_task(app_rocketry.serve())

    # Start both applications (FastAPI & Rocketry)
    print("INFO:\t  Starting applications...")
    await asyncio.wait([scheduler, api])


if __name__ == "__main__":
    asyncio.run(main())
