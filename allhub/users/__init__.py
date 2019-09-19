from .emails import EmailMixin
from .blocking import BlockMixin
from .followers import FollowersMixin
from .gpg_keys import GPGKeysMixin
from .ssh_keys import SSHKeysMixin
from .users import UsersMixin as _UsersMixin
from allhub.util import ConflictCheck


class UsersMixin(
    BlockMixin,
    EmailMixin,
    FollowersMixin,
    GPGKeysMixin,
    SSHKeysMixin,
    _UsersMixin,
    metaclass=ConflictCheck,
):
    pass
