from enum import Enum
from allhub.response import Response

# TODO: Query builder for search is another project. and will taken later.
# TODO: "Query builder" will generate search query in string format.


class Order(Enum):
    ASC = "asc"
    DESC = "desc"


class RepoSort(Enum):
    STARS = "stars"
    FORKS = "forks"
    HELP_WANTED_ISSUES = "help-wanted-issues"
    UPDATED = "updated"
    NONE = None


class CommitSort(Enum):
    AUTHOR_DATE = "author-date"
    COMMITTER_DATE = "committer-date"
    NONE = None


class CodeSort(Enum):
    INDEXED = "indexed"
    NONE = None


class IssueSort(Enum):
    COMMENTS = "comments"
    REACTIONS = "reactions"
    REACTIONS_PLUS = "reactions-+1"
    REACTIONS_MINUS = "reactions--1"
    REACTIONS_SMILE = "reactions_smile"
    REACTIONS_THINKING_FACE = "reactions_thinking_face"
    REACTIONS_HEART = "reactions_heart"
    REACTIONS_TADA = "reactions_tada"
    INTERACTIONS = "interactions"
    CREATED = "created"
    UPDATED = "updated"
    NONE = None


class UserSort(Enum):
    FOLLOWERS = "followers"
    REPOSITORIES = "repositories"
    JOINED = "joined"
    NONE = None


class LabelSort(Enum):
    CREATED = "created"
    UPDATED = "updated"
    NONE = None


class SearchMixin:
    def search_repos(self, q, sort=RepoSort.NONE, order=Order.DESC):
        url = "/search/repositories"
        params = [("q", q), ("order", order.value)]
        if sort.value:
            params.append(("sort", sort.value))
        self.response = Response(
            self.get(
                url,
                params=params,
                **{"Accept": "application/vnd.github.mercy-preview+json"}
            ),
            "Repos",
        )
        return self.response.transform()

    def search_commits(self, q, sort=CommitSort.NONE, order=Order.DESC):
        url = "/search/commits"
        params = [("q", q), ("order", order.value)]
        if sort.value:
            params.append(("sort", sort.value))
        self.response = Response(
            self.get(
                url, params=params, **{"Accept": "application/vnd.github.cloak-preview"}
            ),
            "Commits",
        )
        return self.response.transform()

    def search_code(self, q, sort=CodeSort.NONE, order=Order.DESC):
        url = "/search/code"
        params = [("q", q), ("order", order.value)]
        if sort.value:
            params.append(("sort", sort.value))
        self.response = Response(self.get(url, params=params), "Codes")
        return self.response.transform()

    def search_issues(self, q, sort=IssueSort.NONE, order=Order.DESC):
        url = "/search/issues"
        params = [("q", q), ("order", order.value)]
        if sort.value:
            params.append(("sort", sort.value))
        self.response = Response(
            self.get(
                url,
                params=params,
                **{"Accept": "application/vnd.github.symmetra-preview+json"}
            ),
            "Issues",
        )
        return self.response.transform()

    def search_users(self, q, sort=UserSort.NONE, order=Order.DESC):
        url = "/search/users"
        params = [("q", q), ("order", order.value)]
        if sort.value:
            params.append(("sort", sort.value))
        self.response = Response(
            self.get(
                url,
                params=params,
                **{"Accept": "application/vnd.github.symmetra-preview+json"}
            ),
            "Users",
        )
        return self.response.transform()

    def search_topics(self, q):
        url = "/search/topics"
        params = [("q", q)]
        self.response = Response(
            self.get(
                url,
                params=params,
                **{"Accept": "application/vnd.github.mercy-preview+json"}
            ),
            "Topics",
        )
        return self.response.transform()

    def search_labels(self, repository_id, q, sort=LabelSort.NONE, order=Order.DESC):
        url = "/search/labels"
        params = [
            ("repository_id", int(repository_id)),
            ("q", q),
            ("order", order.value),
        ]
        if sort.value:
            params.append(("sort", sort.value))
        self.response = Response(
            self.get(
                url,
                params=params,
                **{"Accept": "application/vnd.github.symmetra-preview+json"}
            ),
            "Labels",
        )
        return self.response.transform()
