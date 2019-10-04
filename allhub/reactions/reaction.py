from allhub.response import Response
from enum import Enum

_mime_type = "application/vnd.github.squirrel-girl-preview+json"


class ReactionType(Enum):
    PLUS_ONE = "+1"
    MINUS_ONE = "-1"
    LAUGH = "laugh"
    CONFUSED = "confused"
    HEART = "heart"
    HOORAY = "hooray"
    ROCKET = "rocket"
    EYES = "eyes"
    NONE = None


class ReactionMixin:
    def commit_comment_reactions(self, owner, repo, comment_id, content):
        assert isinstance(content, ReactionType)
        url = f"/repos/{owner}/{repo}/comments/{comment_id}/reactions"
        params = {}
        if content.value:
            params = {"content": content.value}
        self.response = Response(
            self.get(url, params=params, **{"Accept": _mime_type}), "Reactions"
        )
        return self.response.transform()

    def create_reaction_commit_comment(self, owner, repo, comment_id, content):
        assert isinstance(content, ReactionType)
        url = f"/repos/{owner}/{repo}/comments/{comment_id}/reactions"
        params = {"content": content.value}
        self.response = Response(
            self.post(url, params=params, **{"Accept": _mime_type}), "Reaction"
        )
        return self.response.transform()

    def reactions_for_issue(self, owner, repo, issue_number, content):
        assert isinstance(content, ReactionType)
        url = f"/repos/{owner}/{repo}/issues/{issue_number}/reactions"
        params = {"content": content.value}
        self.response = Response(
            self.get(url, params=params, **{"Accept": _mime_type}), "Reaction"
        )
        return self.response.transform()

    def create_reaction_for_issue(self, owner, repo, issue_number, content):
        assert isinstance(content, ReactionType)
        url = f"/repos/{owner}/{repo}/issues/{issue_number}/reactions"
        params = {"content": content.value}
        self.response = Response(
            self.post(url, params=params, **{"Accept": _mime_type}), "Reaction"
        )
        return self.response.transform()

    def reactions_for_issue_comment(self, owner, repo, comment_id, content):
        assert isinstance(content, ReactionType)
        url = f"/repos/{owner}/{repo}/issues/comments/{comment_id}/reactions"
        params = {"content": content.value}
        self.response = Response(
            self.get(url, params=params, **{"Accept": _mime_type}), "Reaction"
        )
        return self.response.transform()

    def create_reactions_for_issue_comment(self, owner, repo, comment_id, content):
        assert isinstance(content, ReactionType)
        url = f"/repos/{owner}/{repo}/issues/comments/{comment_id}/reactions"
        params = {"content": content.value}
        self.response = Response(
            self.post(url, params=params, **{"Accept": _mime_type}), "Reaction"
        )
        return self.response.transform()

    def reactions_for_pr_review_comment(self, owner, repo, comment_id, content):
        assert isinstance(content, ReactionType)
        url = f"/repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions"
        params = {"content": content.value}
        self.response = Response(
            self.get(url, params=params, **{"Accept": _mime_type}), "Reaction"
        )
        return self.response.transform()

    def create_reaction_to_pr_review_comment(self, owner, repo, comment_id, content):
        assert isinstance(content, ReactionType)
        url = f"/repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions"
        params = {"content": content.value}
        self.response = Response(
            self.post(url, params=params, **{"Accept": _mime_type}), "Reaction"
        )
        return self.response.transform()

    def reactions_for_team_discussion(self, team_id, discussion_number, content):
        assert isinstance(content, ReactionType)
        url = f"/teams/{team_id}/discussions/{discussion_number}/reactions"
        params = {"content": content.value}
        self.response = Response(
            self.get(
                url,
                params=params,
                **{"Accept": "application/vnd.github.echo-preview+json"},
            ),
            "Reaction",
        )
        return self.response.transform()

    def create_reaction_for_team_discussion(self, team_id, discussion_number, content):
        assert isinstance(content, ReactionType)
        url = f"/teams/{team_id}/discussions/{discussion_number}/reactions"
        params = {"content": content.value}
        self.response = Response(
            self.post(
                url,
                params=params,
                **{"Accept": "application/vnd.github.echo-preview+json"},
            ),
            "Reaction",
        )
        return self.response.transform()

    def reactions_for_team_discussion_comment(
        self, team_id, discussion_number, comment_number, content
    ):
        assert isinstance(content, ReactionType)
        url = f"/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}/reactions"
        params = {"content": content.value}
        self.response = Response(
            self.get(
                url,
                params=params,
                **{"Accept": "application/vnd.github.echo-preview+json"},
            ),
            "Reaction",
        )
        return self.response.transform()

    def create_reaction_for_team_discussion_comment(
        self, team_id, discussion_number, comment_number, content
    ):
        assert isinstance(content, ReactionType)
        url = f"/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}/reactions"
        params = {"content": content.value}
        self.response = Response(
            self.post(
                url,
                params=params,
                **{"Accept": "application/vnd.github.echo-preview+json"},
            ),
            "Reaction",
        )
        return self.response.transform()

    def delete_reaction(self, reaction_id):
        url = f"/reactions/{reaction_id}"
        self.response = Response(
            self.delete(url, **{"Accept": "application/vnd.github.echo-preview+json"}),
            "",
        )
        if self.response.status_code == 204:
            return True
        raise ValueError(
            f"delete_reaction(.....) returned {self.response.status_code}, instead it should return 204"
        )
