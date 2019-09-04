"""
List public events
List repository events
List issue events for a repository
List public events for a network of repositories
List public events for an organization
List events that a user has received
List public events that a user has received
List events performed by a user
List public events performed by a user
List events for an organization

"""
from allhub.response import Response


class EventsMixin:
    def public_events(self):
        url = "/events"
        self.response = Response(self.get(url), "PublicEvents")
        return self.response.transform()

    def repo_events(self, owner, repo):
        url = f"/repos/{owner}/{repo}/events"
        self.response = Response(self.get(url), "RepoEvents")
        return self.response.transform()

    def issue_events(self, owner, repo):
        url = f"/repos/{owner}/{repo}/issues/events"
        self.response = Response(self.get(url), "IssueEvents")
        return self.response.transform()

    def public_events_network_repos(self, owner, repo):
        url = f"/networks/{owner}/{repo}/events"
        self.response = Response(self.get(url), "NetworkRepoPublicEvents")
        return self.response.transform()

    def public_events_orgs(self, org):
        url = f"/orgs/{org}/events"
        self.response = Response(self.get(url), "OrgPublicEvents")
        return self.response.transform()

    def user_received_events(self, username):
        url = f"/users/{username}/received_events"
        self.response = Response(self.get(url), "UserReceivedEvents")
        return self.response.transform()

    def user_received_public_events(self, username):
        url = f"/users/{username}/received_events/public"
        self.response = Response(self.get(url), "UserReceivedPublicEvents")
        return self.response.transform()

    def events_by_user(self, username):
        """
        If you are authenticated as the given user, you will see your private events.
        Otherwise, you'll only see public events.
        :param username:
        :return:
        """
        url = f"/users/{username}/events"
        self.response = Response(self.get(url), "UserEvents")
        return self.response.transform()

    def public_events_by_user(self, username):
        url = f"/users/{username}/received_events"
        self.response = Response(self.get(url), "UserPublicEvents")
        return self.response.transform()

    def events_for_org(self, username, org):
        """
        This is the user's organization dashboard.
        You must be authenticated as the user to view this.
        :param username: username
        :param org: organization
        :return: JSON transformed data.
        """
        url = f"/users/{username}/events/orgs/{org}"
        self.response = Response(self.get(url), "UserReceivedEvents")
        return self.response.transform()
