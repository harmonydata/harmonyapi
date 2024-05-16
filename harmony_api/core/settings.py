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
import base64
import json
from typing import Union

from pydantic import BaseSettings

GOOGLE_APPLICATION_CREDENTIALS: dict = json.loads(
    base64.b64decode(os.getenv("GOOGLE_APPLICATION_CREDENTIALS_B64", "e30="))
)


class Settings(BaseSettings):
    # General harmony_api config
    VERSION: str = "2.0"
    APP_TITLE: str = "Harmony API"
    TIKA_ENDPOINT: str = os.getenv("TIKA_ENDPOINT", "")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    GOOGLE_APPLICATION_CREDENTIALS: dict = GOOGLE_APPLICATION_CREDENTIALS


class DevSettings(Settings):
    SERVER_HOST: str = "0.0.0.0"
    DEBUG: bool = True
    PORT: int = 8000
    RELOAD: bool = True
    CORS: dict = {
        "origins": [
            "*",
        ],
        "allow_credentials": True,
        "allow_methods": ["*"],
        "allow_headers": ["*"],
    }


class ProdSettings(Settings):
    # TODO change
    SERVER_HOST: str = "0.0.0.0"
    DEBUG: bool = False
    PORT: int = 8000
    RELOAD: bool = False
    CORS: dict = {
        "origins": [
            "*",
        ],
        "allow_credentials": True,
        "allow_methods": ["*"],
        "allow_headers": ["*"],
    }


def get_settings():
    env = os.getenv("STAGE", "dev")
    settings_type = {
        "dev": DevSettings(),
        "prod": ProdSettings(),
    }
    return settings_type[env]


settings: Union[DevSettings | ProdSettings] = get_settings()
