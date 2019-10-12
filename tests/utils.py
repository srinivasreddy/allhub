from allhub import AllHub
import os

allhub = AllHub(
    os.environ.get("GH_USERNAME"),
    os.environ.get("GH_TOKEN"),
    password=os.environ.get("GH_PASSWORD"),
)
