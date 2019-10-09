from enum import Enum


class InteractionLimit(Enum):
    EXISTING_USERS = "existing_users"
    CONTRIBUTORS_ONLY = "contributors_only"
    COLLABORATORS_ONLY = "collaborators_only"
