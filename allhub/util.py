import sys
from distutils.spawn import find_executable
import subprocess
from enum import Enum


def check_git_installed():
    # TODO: move to utils.
    git_location = find_executable("git")
    if git_location is None:
        sys.stderr.write(
            "git is not installed. " "Please install git for your operating system.\n"
        )
        sys.exit(-1)


class MimeType(Enum):
    Json = "json"
    Text = "text"


def shell_git_clone(_url):
    # TODO: How to recover from the network failure, existing repos??
    command = f"git clone {_url}"
    subprocess.call(
        command,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        shell=True,
    )
