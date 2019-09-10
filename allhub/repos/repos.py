from allhub.response import Response

from enum import Enum


class Visibility(Enum):
    ALL = "all"
    PUBLIC = "public"
    PRIVATE = "private"


class Sort(Enum):
    CREATED = "created"
    UPDATED = "updated"
    PUSHED = "pushed"
    FULLNAME = "full_name"


class Type(Enum):
    ALL = "all"
    OWNER = "owner"
    PUBLIC = "public"
    PRIVATE = "private"
    MEMBER = "member"


class Affiliation(Enum):
    OWNER = "owner"
    COLLABORATOR = "collaborator"
    ORGANIZATION_MEMBER = "organization_member"


class Direction(Enum):
    ASC = "asc"
    DESC = "desc"


_affiliation = f"{Affiliation.OWNER.value},{Affiliation.COLLABORATOR.value},{Affiliation.ORGANIZATION_MEMBER.value}"


class ReposMixin:
    def repos(
        self,
        visibility=Visibility.ALL,
        affiliation=_affiliation,
        type=Type.ALL,
        sort=Sort.FULLNAME,
        direction=Direction.DESC,
    ):
        """
        Lists repositories that the authenticated user has explicit permission
        (:read, :write, or :admin) to access.
        """
        if not isinstance(visibility, Visibility):
            raise ValueError("visibility should be Visibility type")
        if visibility not in Visibility:
            raise ValueError("visibility should either be 'ALL','PUBLIC', or 'PRIVATE'")
        for aff in affiliation.split(","):
            if aff not in ("owner", "collaborator" "organization_member"):
                raise ValueError(
                    f"{aff} should either be 'owner', 'collaborator', 'organization_member'"
                )
        if not isinstance(type, Type):
            raise ValueError("type should be instance of Type")
        if type not in Type:
            raise ValueError(
                "type should either be 'ALL', 'OWNER', 'PUBLIC', 'PRIVATE', or 'MEMBER'"
            )

        if not isinstance(sort, Sort):
            raise ValueError("sort should be instance of Sort")
        if sort not in Sort:
            raise ValueError(
                "sort should either be 'CREATED', 'UPDATED', 'PUSHED', or 'FULLNAME'"
            )

        if not isinstance(direction, Direction):
            raise ValueError("direction should be instance of Direction")
        if direction not in Direction:
            raise ValueError("direction should either be 'ASC', or 'DESC'")

        url = "/user/repos"
        params = [
            ("visibility", visibility.value),
            ("affiliation", affiliation),
            ("type", type.value),
            ("sort", sort.value),
            ("direction", direction.value),
        ]
        self.response = Response(self.get_basic(url, params=params), "Repos")
        return self.response.transform()
