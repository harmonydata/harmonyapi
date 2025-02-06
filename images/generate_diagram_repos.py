
from diagrams import Cluster, Diagram
from diagrams.azure.compute import AppServices
from diagrams.aws.database import ElastiCache, RDS
from diagrams.aws.network import ELB
from diagrams.aws.network import Route53
from diagrams.generic.os import Ubuntu
from diagrams.generic.device import Tablet
from diagrams.programming.language import Python, Java, R
from diagrams.programming.framework import Fastapi
from diagrams.onprem.container import Docker

with Diagram("Harmony repositories", show=False):
    py = Python("Python repository\npip install harmonydata\ngithub.com/\nharmonydata/\nharmony")
    fastapi = Fastapi("FastAPI repository\ngithub.com/\nharmonydata/\nharmonyapi")
    browser = Tablet("Front end repository\ngithub.com/\nharmonydata/\napp")
    r = R("R library\ngithub.com/\nharmonydata/\nharmony_r")

    py << fastapi << browser
    fastapi << r
