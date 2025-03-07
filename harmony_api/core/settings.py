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

import os
from typing import Union

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # General harmony_api config
    VERSION: str = Field(description="Application version.", default="2.0")
    APP_TITLE: str = Field(description="Application title.", default="Harmony API")
    TIKA_ENDPOINT: str = Field(description="Tika endpoint.", default="http://tika:9998")
    OPENAI_API_KEY: str | None = Field(description="OpenAI API key.", default=None)
    AZURE_OPENAI_API_KEY: str | None = Field(description="Azure OpenAI API key.", default=None)
    AZURE_OPENAI_ENDPOINT: str | None = Field(description="Azure OpenAI endpoint.", default=None)
    AZURE_STORAGE_URL: str | None = Field(description="Azure Storage URL.", default=None)
    GOOGLE_APPLICATION_CREDENTIALS: str | None = Field(
        description="A JSON string is expected here, this is the content of credentials.json.",
        default=None
    )


class DevSettings(Settings):
    SERVER_HOST: str = Field(description="Host.", default="0.0.0.0")
    DEBUG: bool = Field(description="Debug.", default=True)
    PORT: int = Field(description="Port.", default=8000)
    RELOAD: bool = Field(description="Reload.", default=True)
    CORS: dict = Field(description="CORS.", default={
        "origins": [
            "*",
        ],
        "allow_credentials": True,
        "allow_methods": ["*"],
        "allow_headers": ["*"],
    })


class ProdSettings(Settings):
    # TODO change
    SERVER_HOST: str = Field(description="Host.", default="0.0.0.0")
    DEBUG: bool = Field(description="Debug.", default=False)
    PORT: int = Field(description="Port.", default=8000)
    RELOAD: bool = Field(description="Reload.", default=False)
    CORS: dict = Field(description="CORS.", default={
        "origins": [
            "*",
        ],
        "allow_credentials": True,
        "allow_methods": ["*"],
        "allow_headers": ["*"],
    })


def get_settings() -> Union[DevSettings | ProdSettings]:
    env = os.getenv("STAGE", "dev")
    settings_type = {
        "dev": DevSettings(),
        "prod": ProdSettings(),
    }
    return settings_type[env]


settings: Union[DevSettings | ProdSettings] = get_settings()
