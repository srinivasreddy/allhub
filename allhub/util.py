import subprocess
import sys
from distutils.spawn import find_executable
from enum import Enum
from collections import Counter


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
            data = "\n".join([f"{key}: {count}" for key, count in conflict_names])
            raise ValueError(
                f"The following methods defined more than once.\n {data}\n"
                f"Please choose other names for your methods."
            )
        return super(ConflictCheck, mcs).__new__(mcs, name, bases, dikt)


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
