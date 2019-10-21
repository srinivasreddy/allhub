from allhub.response import Response
from enum import Enum

_mime_type = "application/vnd.github.squirrel-girl-preview+json"
team_discussion_mime = {"Accept": "application/vnd.github.echo-preview+json"}


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
        url = "/repos/{owner}/{repo}/comments/{comment_id}/reactions".format(
            owner=owner, repo=repo, comment_id=comment_id
        )
        params = {}
        if content.value:  # can be None
            params = {"content": content.value}
        self.response = Response(
            self.get(url, params=params, **{"Accept": _mime_type}), "Reactions"
        )
        return self.response.transform()

    def create_reaction_commit_comment(self, owner, repo, comment_id, content):
        assert isinstance(content, ReactionType)
        url = "/repos/{owner}/{repo}/comments/{comment_id}/reactions".format(
            owner=owner, repo=repo, comment_id=comment_id
        )
        params = {"content": content.value}
        self.response = Response(
            self.post(url, params=params, **{"Accept": _mime_type}), "Reaction"
        )
        return self.response.transform()

    def reactions_for_issue(self, owner, repo, issue_number, content):
        assert isinstance(content, ReactionType)
        url = "/repos/{owner}/{repo}/issues/{issue_number}/reactions".format(
            owner=owner, repo=repo, issue_number=issue_number
        )
        params = {"content": content.value}
        self.response = Response(
            self.get(url, params=params, **{"Accept": _mime_type}), "Reaction"
        )
        return self.response.transform()

    def create_reaction_for_issue(self, owner, repo, issue_number, content):
        assert isinstance(content, ReactionType)
        url = "/repos/{owner}/{repo}/issues/{issue_number}/reactions"
        params = {"content": content.value}
        self.response = Response(
            self.post(url, params=params, **{"Accept": _mime_type}), "Reaction"
        )
        return self.response.transform()

    def reactions_for_issue_comment(self, owner, repo, comment_id, content):
        assert isinstance(content, ReactionType)
        url = "/repos/{owner}/{repo}/issues/comments/{comment_id}/reactions".format(
            owner=owner, repo=repo, comment_id=comment_id
        )
        params = {"content": content.value}
        self.response = Response(
            self.get(url, params=params, **{"Accept": _mime_type}), "Reaction"
        )
        return self.response.transform()

    def create_reactions_for_issue_comment(self, owner, repo, comment_id, content):
        assert isinstance(content, ReactionType)
        url = "/repos/{owner}/{repo}/issues/comments/{comment_id}/reactions".format(
            owner=owner, repo=repo, comment_id=comment_id
        )
        params = {"content": content.value}
        self.response = Response(
            self.post(url, params=params, **{"Accept": _mime_type}), "Reaction"
        )
        return self.response.transform()

    def reactions_for_pr_review_comment(self, owner, repo, comment_id, content):
        assert isinstance(content, ReactionType)
        url = "/repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions".format(
            owner=owner, repo=repo, comment_id=comment_id
        )
        params = {"content": content.value}
        self.response = Response(
            self.get(url, params=params, **{"Accept": _mime_type}), "Reaction"
        )
        return self.response.transform()

    def create_reaction_to_pr_review_comment(self, owner, repo, comment_id, content):
        assert isinstance(content, ReactionType)
        url = "/repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions".format(
            owner=owner, repo=repo, comment_id=comment_id
        )
        params = {"content": content.value}
        self.response = Response(
            self.post(url, params=params, **{"Accept": _mime_type}), "Reaction"
        )
        return self.response.transform()

    def reactions_for_team_discussion(self, team_id, discussion_number, content):
        assert isinstance(content, ReactionType)
        url = "/teams/{team_id}/discussions/{discussion_number}/reactions".format(
            team_id=team_id, discussion_number=discussion_number
        )
        params = {"content": content.value}
        self.response = Response(
            self.get(url, params=params, **team_discussion_mime), "Reaction"
        )
        return self.response.transform()

    def create_reaction_for_team_discussion(self, team_id, discussion_number, content):
        assert isinstance(content, ReactionType)
        url = "/teams/{team_id}/discussions/{discussion_number}/reactions".format(
            team_id=team_id, discussion_number=discussion_number
        )
        params = {"content": content.value}
        self.response = Response(
            self.post(url, params=params, **team_discussion_mime), "Reaction"
        )
        return self.response.transform()

    def reactions_for_team_discussion_comment(
        self, team_id, discussion_number, comment_number, content
    ):
        assert isinstance(content, ReactionType)
        url = "/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}/reactions".format(
            team_id=team_id,
            discussion_number=discussion_number,
            comment_number=comment_number,
        )
        params = {"content": content.value}
        self.response = Response(
            self.get(url, params=params, **team_discussion_mime), "Reaction"
        )
        return self.response.transform()

    def create_reaction_for_team_discussion_comment(
        self, team_id, discussion_number, comment_number, content
    ):
        assert isinstance(content, ReactionType)
        url = "/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}/reactions".format(
            team_id=team_id,
            discussion_number=discussion_number,
            comment_number=comment_number,
        )
        params = {"content": content.value}
        self.response = Response(
            self.post(url, params=params, **team_discussion_mime), "Reaction"
        )
        return self.response.transform()

    def delete_reaction(self, reaction_id):
        url = "/reactions/{reaction_id}".format(reaction_id=reaction_id)
        self.response = Response(self.delete(url, **team_discussion_mime), "")
        if self.response.status_code == 204:
            return True
        raise ValueError(
            "delete_reaction(.....) returned {status_code}, instead it should return 204".format(
                status_code=self.response.status_code
            )
        )
