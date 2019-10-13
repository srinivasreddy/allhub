from allhub.response import Response

_mime = ", ".join(
    [
        "application/vnd.github.echo-preview+json",
        "application/vnd.github.squirrel-girl-preview",
    ]
)
from enum import Enum


class TeamDiscussionCommentDirection(Enum):
    ASC = "asc"
    DSC = "dsc"


class TeamDiscussionCommentsMixin:
    def team_discussion_comments(
        self, team_id, discussion_number, direction=TeamDiscussionCommentDirection.DSC
    ):
        url = "/teams/{team_id}/discussions/{discussion_number}/comments".format(
            team_id=team_id, discussion_number=discussion_number
        )
        params = {"direction": direction.value}
        self.response = Response(
            self.get(url, params=params, **{"Accept": _mime}), "OrgTeam"
        )
        return self.response.transform()

    def team_discussion_comment(
        self,
        team_id,
        discussion_number,
        comment_number,
        direction=TeamDiscussionCommentDirection.DSC,
    ):
        url = "/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}".format(
            team_id=team_id,
            discussion_number=discussion_number,
            comment_number=comment_number,
        )
        params = {"direction": direction.value}
        self.response = Response(
            self.get(url, params=params, **{"Accept": _mime}), "OrgTeam"
        )
        return self.response.transform()

    def create_team_discussion_comment(self, team_id, discussion_number, body):
        url = "/teams/{team_id}/discussions/{discussion_number}/comments".format(
            team_id=team_id, discussion_number=discussion_number
        )
        params = {"body": body}
        self.response = Response(
            self.post(url, params=params, **{"Accept": _mime}), "OrgTeam"
        )
        return self.response.transform()

    def edit_team_discussion_comment(
        self, team_id, discussion_number, comment_number, body
    ):
        url = "/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}".format(
            team_id=team_id,
            discussion_number=discussion_number,
            comment_number=comment_number,
        )
        params = {"body": body}
        self.response = Response(
            self.patch(url, params=params, **{"Accept": _mime}), "OrgTeam"
        )
        return self.response.transform()

    def delete_team_discussion_comment(
        self, team_id, discussion_number, comment_number
    ):
        url = "/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}".format(
            team_id=team_id,
            discussion_number=discussion_number,
            comment_number=comment_number,
        )
        self.response = Response(self.delete(url, **{"Accept": _mime}), "")
        return self.response.status_code == 204
