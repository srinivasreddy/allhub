# flake8: NOQA
from .organization import OrganizationMigrationMixin
from .source_imports import SourceImportMixin
from .user import UserMigrationMixin
from allhub.util import ConflictCheck


class MigrationMixin(
    OrganizationMigrationMixin,
    SourceImportMixin,
    UserMigrationMixin,
    metaclass=ConflictCheck,
):
    pass
