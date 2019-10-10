from .blobs import BlobMixin
from .commits import CommitMixin
from .references import ReferencesMixin
from .tags import TagsMixin
from .trees import TreesMixin
from allhub.util import ConflictCheck


class GitDataMixin(
    BlobMixin,
    CommitMixin,
    ReferencesMixin,
    TagsMixin,
    TreesMixin,
    metaclass=ConflictCheck,
):
    pass
