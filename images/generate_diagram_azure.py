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
from diagrams.azure.compute import FunctionApps

with Diagram("Harmony architecture Azure", show=False):
    browser = Tablet("Front end (React)")
    with Cluster("harmonyvirtualnetwork"):
        fastapi = AppServices("harmonyapi\nApp service")
        tika = AppServices("harmonytika\nApp service")
        f = FunctionApps("harmonyspacy\nFunction app wrapping spaCy")
        storage = BlobStorage("harmonystorage\nStorage account")

    browser >> fastapi >> tika
    fastapi >> f
    fastapi >> storage
