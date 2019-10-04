from .coc import CodeOfConductMixin
from .emoji import EmojiMixin
from .gitignore import GitIgnoreMixin
from .license import LicenseMixin
from .markdown import MarkDownMixin
from .meta import MetaMixin
from .rate_limit import RateLimitMixin

from allhub.util import ConflictCheck


class MiscellaneousMixin(
    CodeOfConductMixin,
    EmojiMixin,
    GitIgnoreMixin,
    LicenseMixin,
    MarkDownMixin,
    MetaMixin,
    RateLimitMixin,
    metaclass=ConflictCheck,
):
    pass
