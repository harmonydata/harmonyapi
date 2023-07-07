import json
import os
from hashlib import sha256

from azure.storage.blob import ContainerClient, BlobClient

import constants

AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
CONTAINER_NAME = "harmonycache"


def get_hash_value(text: str) -> str:
    """Get hash value"""

    return sha256(text.encode()).hexdigest()


def get_container_harmonycache() -> ContainerClient:
    """Get container 'harmonycache'"""

    return ContainerClient.from_connection_string(
        conn_str=AZURE_STORAGE_CONNECTION_STRING,
        container_name=CONTAINER_NAME,
    )


def get_cache_from_azure(cache_file_name: str) -> dict:
    """Get cache from Azure Blob Storage"""

    cache = {}

    blob = BlobClient.from_connection_string(
        conn_str=AZURE_STORAGE_CONNECTION_STRING,
        container_name=CONTAINER_NAME,
        blob_name=cache_file_name,
    )

    if blob.exists():
        try:
            cache = json.loads(blob.download_blob().readall().decode())
        except (Exception,) as e:
            print(f"ERROR:\t  Could not get cache from Azure Blob Storage: {str(e)}")

    return cache


def save_cache_to_azure(cache: dict, cache_file_name: str):
    """Save cache to Azure Blob Storage"""

    container_harmonycache = get_container_harmonycache()

    try:
        container_harmonycache.upload_blob(
            name=cache_file_name, data=json.dumps(cache), overwrite=True
        )
        print("INFO:\t  Cache saved to Azure Blob Storage")
    except (Exception,) as e:
        print(f"ERROR:\t  Could not save cache to Azure Blob Storage: {str(e)}")


def clear_all_cache():
    """Clear cache"""

    container = get_container_harmonycache()

    container.delete_blob(blob=constants.INSTRUMENTS_CACHE_JSON_FILENAME)
