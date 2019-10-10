from allhub.response import Response

_mime = ", ".join(
    [
        "application/vnd.github.echo-preview+json",
        "application/vnd.github.squirrel-girl-preview",
    ]
)


class TeamDiscussionsMixin:
    def team_discussions(self, team_id):
        url = f"/teams/{team_id}/discussions"
        self.response = Response(self.get(url, **{"Accept": _mime}), "TeamDiscussions")
        return self.response.transform()

    def team_discussion(self, team_id, discussion_number):
        url = f"/teams/{team_id}/discussions/{discussion_number}"
        self.response = Response(self.get(url, **{"Accept": _mime}), "TeamDiscussion")
        return self.response.transform()

    def create_team_discussion(self, team_id, title, body, private=False):
        url = f"/teams/{team_id}/discussions"
        params = {"title": title, "body": body, "private": private}
        self.response = Response(
            self.post(url, params=params, **{"Accept": _mime}), "TeamDiscussion"
        )
        return self.response.transform()

    def edit_team_discussion(self, team_id, discussion_number, title, body):
        url = f"/teams/{team_id}/discussions/{discussion_number}"
        params = {"title": title, "body": body}
        self.response = Response(
            self.patch(url, params=params, **{"Accept": _mime}), "TeamDiscussion"
        )
        return self.response.transform()

    def delete_team_discussion(self, team_id, discussion_number):
        url = f"/teams/{team_id}/discussions/{discussion_number}"
        self.response = Response(self.delete(url, **{"Accept": _mime}), "")
        return self.response.status_code == 204
