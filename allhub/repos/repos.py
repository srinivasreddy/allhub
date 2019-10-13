from allhub.response import Response

from enum import Enum


class RepoVisibility(Enum):
    ALL = "all"
    PUBLIC = "public"
    PRIVATE = "private"


class RepoSort(Enum):
    CREATED = "created"
    UPDATED = "updated"
    PUSHED = "pushed"
    FULLNAME = "full_name"


class RepoType(Enum):
    ALL = "all"
    OWNER = "owner"
    PUBLIC = "public"
    PRIVATE = "private"
    MEMBER = "member"


class RepoAffiliation(Enum):
    OWNER = "owner"
    COLLABORATOR = "collaborator"
    ORGANIZATION_MEMBER = "organization_member"


class RepoDirection(Enum):
    ASC = "asc"
    DESC = "desc"


_affiliation = "{RepoAffiliation.OWNER.value},{RepoAffiliation.COLLABORATOR.value},{RepoAffiliation.ORGANIZATION_MEMBER.value}"


class ReposMixin:
    def repos(self, **kwargs):
        """
        Lists repositories that the authenticated user has explicit permission
        (:read, :write, or :admin) to access.

        The authenticated user has explicit permission to access repositories they own,
        repositories where they are a collaborator, and repositories that they can access
        through an organization membership.
        """
        params = []
        if "visibility" in kwargs:
            visibility = kwargs.pop("visibility")
            if not isinstance(visibility, RepoVisibility):
                raise ValueError(
                    "'{visibility}' should be instance Visibility".format(
                        visibility=visibility
                    )
                )
            if visibility not in RepoVisibility:
                raise ValueError(
                    "'{visibility}' should either be 'ALL','PUBLIC', or 'PRIVATE'".format(
                        visibility=visibility
                    )
                )
            params.append(("visibility", visibility.value))
        if "affiliation" in kwargs:
            affiliation = kwargs.pop("affiliation")
            for aff in affiliation.split(","):
                if aff not in ("owner", "collaborator", "organization_member"):
                    raise ValueError(
                        "'{aff}' should either be 'owner', 'collaborator', or 'organization_member'".format(
                            aff=aff
                        )
                    )
            params.append(("affiliation", affiliation))
        if "type" in kwargs and ("visibility" in kwargs or "affiliation" in kwargs):
            raise AttributeError(
                "If you specify visibility or affiliation, you cannot specify type."
            )
        if "type" in kwargs:
            type = kwargs.pop("type")
            if not isinstance(type, RepoType):
                raise ValueError(
                    "'{type}' should be instance of Type".format(type=type)
                )
            if type not in RepoType:
                raise ValueError(
                    "'{type}' should either be 'ALL', 'OWNER', 'PUBLIC', 'PRIVATE', or 'MEMBER'".format(
                        type=type
                    )
                )
            params.append(("type", type.value))
        if "sort" in kwargs:
            sort = kwargs.pop("sort")
            if not isinstance(sort, RepoSort):
                raise ValueError("{sort} should be instance of Sort".format(sort=sort))
            if sort not in RepoSort:
                raise ValueError(
                    "'{sort}' should either be 'CREATED', 'UPDATED', 'PUSHED', or 'FULLNAME'".format(
                        sort=sort
                    )
                )
            params.append(("sort", sort.value))
        if "direction" in kwargs:
            direction = kwargs.pop("direction")
            if not isinstance(direction, RepoDirection):
                raise ValueError(
                    "'{direction}' is not an instance of Direction".format(
                        direction=direction
                    )
                )
            if direction not in RepoDirection:
                raise ValueError(
                    "'{direction}' should either be 'ASC', or 'DESC'".format(
                        direction=direction
                    )
                )
            params.append(("direction", direction.value))
        url = "/user/repos"
        self.response = Response(self.get_basic(url, params=params, **kwargs), "Repos")
        return self.response.transform()

    def user_repos(self, username, **kwargs):
        params = []
        if "type" in kwargs:
            type = kwargs.pop("type")
            if not isinstance(type, RepoType):
                raise ValueError(
                    "'{type}' should be instance of Type".format(type=type)
                )
            if type not in RepoType:
                raise ValueError(
                    "'{type}' should either be 'ALL', 'OWNER', 'PUBLIC', 'PRIVATE', or 'MEMBER'".format(
                        type=type
                    )
                )
            params.append(("type", type.value))
        if "sort" in kwargs:
            sort = kwargs.pop("sort")
            if not isinstance(sort, RepoSort):
                raise ValueError("{sort} should be instance of Sort".format(sort=sort))
            if sort not in RepoSort:
                raise ValueError(
                    "'{sort}' should either be 'CREATED', 'UPDATED', 'PUSHED', or 'FULLNAME'".format(
                        sort=sort
                    )
                )
            params.append(("sort", sort.value))
        if "direction" in kwargs:
            direction = kwargs.pop("direction")
            if not isinstance(direction, RepoDirection):
                raise ValueError(
                    "'{direction}' is not an instance of Direction".format(
                        direction=direction
                    )
                )
            if direction not in RepoDirection:
                raise ValueError(
                    "'{direction}' should either be 'ASC', or 'DESC'".format(
                        direction=direction
                    )
                )
            params.append(("direction", direction.value))
        url = "/users/{username}/repos".format(username=username)
        self.response = Response(self.get_basic(url, params=params, **kwargs), "Repos")
        return self.response.transform()

    def org_repos(self, org, **kwargs):
        params = []
        if "type" in kwargs:
            type = kwargs.pop("type")
            if not isinstance(type, RepoType):
                raise ValueError("'{type}' should be instance of Type")
            if type not in RepoType:
                raise ValueError(
                    "'{type}' should either be 'ALL', 'OWNER', 'PUBLIC', 'PRIVATE', or 'MEMBER'"
                )
            params.append(("type", type.value))
        if "sort" in kwargs:
            sort = kwargs.pop("sort")
            if not isinstance(sort, RepoSort):
                raise ValueError("{sort} should be instance of Sort")
            if sort not in RepoSort:
                raise ValueError(
                    "'{sort}' should either be 'CREATED', 'UPDATED', 'PUSHED', or 'FULLNAME'"
                )
            params.append(("sort", sort.value))
        if "direction" in kwargs:
            direction = kwargs.pop("direction")
            if not isinstance(direction, RepoDirection):
                raise ValueError("'{direction}' is not an instance of Direction")
            if direction not in RepoDirection:
                raise ValueError("'{direction}' should either be 'ASC', or 'DESC'")
            params.append(("direction", direction.value))
        url = "/users/{org}/repos".format(org=org)
        self.response = Response(self.get_basic(url, params=params, **kwargs), "Repos")
        return self.response.transform()

    def all_repos(self, **kwargs):
        url = "/repositories"
        params = []
        if "since" in kwargs:
            since = kwargs.pop("since")
            params.append(("since", since))
        self.response = Response(self.get_basic(url, params=params, **kwargs), "Repos")
        return self.response.transform()
