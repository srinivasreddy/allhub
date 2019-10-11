from allhub import AllHub
import os

allhub = AllHub(
    os.environ.get("USERNAME"),
    os.environ.get("TOKEN"),
    password=os.environ.get("PASSWORD"),
)
