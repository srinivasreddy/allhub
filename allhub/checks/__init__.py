from .check_runs import CheckRunsMixin
from .check_suites import CheckSuitesMixin
from allhub.util import ConflictCheck


class CheckMixin(CheckRunsMixin, CheckSuitesMixin, metaclass=ConflictCheck):
    pass
