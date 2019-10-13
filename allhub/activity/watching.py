from allhub.response import Response


class WatchingMixin:
    def list_watchers(self, owner, repo, **kwargs):
        url = "/repos/{owner}/{repo}/subscribers".format(owner=owner, repo=repo)
        self.response = Response(self.get(url, **kwargs), "Watchers")
        return self.response.transform()

    def repos_watched_by(self, username, **kwargs):
        url = "/users/{username}/subscriptions".format(username=username)
        self.response = Response(self.get(url, **kwargs), "WatchedRepos")
        return self.response.transform()

    def repos_watched(self, **kwargs):
        url = "/user/subscriptions"
        self.response = Response(self.get(url, **kwargs), "WatchedRepos")
        return self.response.transform()

    def repo_subscription(self, owner, repo, **kwargs):
        url = "/repos/{owner}/{repo}/subscription".format(owner=owner, repo=repo)
        self.response = Response(self.get(url, **kwargs), "RepoSubscription")
        return self.response.transform()

    def set_subscription(self, owner, repo, subscribed=True, ignored=False, **kwargs):
        url = "repos/{owner}/{repo}/subscription".format(owner=owner, repo=repo)
        params = [("subscribed", subscribed), ("ignored", ignored)]
        self.response = Response(self.put(url, params=params, **kwargs), "Subscription")
        return self.response.transform()

    def delete_subscription(self, owner, repo, **kwargs):
        url = "repos/{owner}/{repo}/subscription".format(owner=owner, repo=repo)
        self.response = Response(self.delete(url, **kwargs), "")
        return self.response.status_code == 204

    # TODO: The following legacy APIs are left out. Raise a PR if you like them to be here.
    # https://developer.github.com/v3/activity/watching/#check-if-you-are-watching-a-repository-legacy
    # https://developer.github.com/v3/activity/watching/#watch-a-repository-legacy
    # https://developer.github.com/v3/activity/watching/#stop-watching-a-repository-legacy
