import justpy as jp

import documentation
from api import Api

jp.Route("/api", Api.serve)
jp.Route("/", documentation.Doc.serve)
jp.justpy()
