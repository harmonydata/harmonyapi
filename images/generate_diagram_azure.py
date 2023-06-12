from diagrams import Cluster, Diagram
from diagrams.azure.compute import AppServices
from diagrams.aws.database import ElastiCache, RDS
from diagrams.aws.network import ELB
from diagrams.aws.network import Route53
from diagrams.generic.os import Ubuntu
from diagrams.generic.device import Tablet
from diagrams.programming.language import Python, Java
from diagrams.onprem.container import Docker
from diagrams.onprem.inmemory import Redis
from diagrams.azure.compute import FunctionApps
from diagrams.azure.compute import AppServices
from diagrams.azure.database import BlobStorage

with Diagram("Harmony architecture Azure", show=False):
    browser = Tablet("Front end (React)")
    with Cluster("harmonyvirtualnetwork"):
        fastapi = AppServices("harmonyapi\nApp service")
        tika = AppServices("harmonytika\nApp service")
        redis = Redis("harmonyredis\nAzure Cache for Redis")
        storage = BlobStorage("harmonystorage\nStorage account")

    browser >> fastapi >> tika
    fastapi >> redis
    fastapi >> storage
