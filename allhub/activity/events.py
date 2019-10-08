from allhub.response import Response


class EventsMixin:
    """
    This is a readonly interface to events.
    Ref. https://developer.github.com/v3/activity/events/
    """

    def public_events(self, **headers):
        """
        List public events.
        """
        url = "/events"
        self.response = Response(self.get(url, **headers), "PublicEvents")
        return self.response.transform()

    def repo_events(self, owner, repo, **headers):
        """
        List repository events.
        """
        url = f"/repos/{owner}/{repo}/events"
        self.response = Response(self.get(url, **headers), "RepoEvents")
        return self.response.transform()

    def issue_events(self, owner, repo, **headers):
        """
        List issue events for a repository.
        """
        url = f"/repos/{owner}/{repo}/issues/events"
        self.response = Response(self.get(url, **headers), "IssueEvents")
        return self.response.transform()

    def public_events_network_repos(self, owner, repo, **headers):
        """
        List public events for a network of repositories.
        """
        url = f"/networks/{owner}/{repo}/events"
        self.response = Response(self.get(url, **headers), "NetworkRepoPublicEvents")
        return self.response.transform()

    def public_events_orgs(self, org, **headers):
        """
        List public events for an organization.
        """
        url = f"/orgs/{org}/events"
        self.response = Response(self.get(url, **headers), "OrgPublicEvents")
        return self.response.transform()

    def user_received_events(self, username, **headers):
        """
        List events that a user has received.
        """
        url = f"/users/{username}/received_events"
        self.response = Response(self.get(url, **headers), "UserReceivedEvents")
        return self.response.transform()

    def user_received_public_events(self, username, **headers):
        """
        List public events that a user has received.
        """
        url = f"/users/{username}/received_events/public"
        self.response = Response(self.get(url, **headers), "UserReceivedPublicEvents")
        return self.response.transform()

    def events_by_user(self, username, **kwargs):
        """
        List events performed by a user.

        If you are authenticated as the given user, you will see your private events.
        Otherwise, you'll only see public events.
        """
        url = f"/users/{username}/events"
        self.response = Response(self.get(url, **kwargs), "UserEvents")
        return self.response.transform()

    def public_events_by_user(self, username, **kwargs):
        """
        List public events performed by a user
        """
        url = f"/users/{username}/received_events"
        self.response = Response(self.get(url, **kwargs), "UserPublicEvents")
        return self.response.transform()

    def events_for_org(self, username, org, **kwargs):
        """
        List events for an organization.

        This is the user's organization dashboard.
        You must be authenticated as the user to view this.
        """
        url = f"/users/{username}/events/orgs/{org}"
        self.response = Response(self.get(url, **kwargs), "UserReceivedEvents")
        return self.response.transform()
