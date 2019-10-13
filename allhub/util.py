import subprocess
import sys
from distutils.spawn import find_executable
from enum import Enum
from collections import Counter

from dataclasses import dataclass


@dataclass()
class Config:
    api_version = 3
    api_mime_type = "json"


config = Config()


class MediaType(Enum):
    RAW = "application/vnd.github.{version}.raw+json".format(version=config.api_version)
    TEXT = "application/vnd.github.{version}.text+json".format(
        version=config.api_version
    )
    HTML = "application/vnd.github.{version}.html+json".format(
        version=config.api_version
    )
    FULL = "application/vnd.github.{version}.full+json".format(
        version=config.api_version
    )
    JSON = "application/vnd.github.{version}+json".format(version=config.api_version)
    NONE = None


class ErrorAPICode(Exception):
    pass


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


def validate_iso8601_string(string):
    return True
    # raise an exception otherwise.


class ConflictCheck(type):
    def __new__(mcs, name, bases, dikt):
        object_methods = {}
        counter = Counter()
        for base in bases:
            method_names = [a for a in dir(base) if not a.startswith("__")]
            counter.update(method_names)
            object_methods[base.__name__] = method_names
        conflict_names = [
            (key, count) for (key, count) in counter.most_common() if count != 1
        ]
        if conflict_names:
            data = "\n".join(
                ["{}: {}".format(key, count) for key, count in conflict_names]
            )
            raise ValueError(
                "The following methods defined more than once.\n {data}\n"
                "Please choose other names for your methods.".format(data=data)
            )
        return super(ConflictCheck, mcs).__new__(mcs, name, bases, dikt)


def shell_git_clone(_url):
    # TODO: How to recover from the network failure, existing repos??
    command = "git clone {_url}".format(_url=_url)
    subprocess.call(
        command,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        shell=True,
    )
