from allhub.response import Response


class WebHooksMixin:
    def repo_hooks(self, owner, repo):
        url = "/repos/{owner}/{repo}/hooks".format(owner=owner, repo=repo)
        self.response = Response(self.get(url), "Hooks")
        return self.response.transform()

    def repo_hook(self, owner, repo, hook_id):
        url = "/repos/{owner}/{repo}/hooks/{hook_id}".format(
            owner=owner, repo=repo, hook_id=hook_id
        )
        self.response = Response(self.get(url), "Hook")
        return self.response.transform()

    def create_repo_hook(self, owner, repo, config, events, name="web", active=True):
        url = "/repos/{owner}/{repo}/hooks".format(owner=owner, repo=repo)
        assert isinstance(config, dict)
        assert isinstance(events, (list, tuple))
        params = {"name": name, "active": active, "events": events, "config": config}
        self.response = Response(self.post(url, params=params), "Hook")
        return self.response.transform()

    def edit_repo_hook(
        self,
        owner,
        repo,
        hook_id,
        config,
        events,
        add_events,
        remove_events,
        active=True,
    ):
        url = "/repos/{owner}/{repo}/hooks/{hook_id}".format(
            owner=owner, repo=repo, hook_id=hook_id
        )
        assert isinstance(config, dict)
        assert isinstance(events, (list, tuple))
        params = {
            "active": active,
            "events": events,
            "add_events": add_events,
            "remove_events": remove_events,
            "config": config,
        }
        self.response = Response(self.patch(url, params=params), "Hook")
        return self.response.transform()

    def test_repo_push_hook(self, owner, repo, hook_id):
        url = "/repos/{owner}/{repo}/hooks/{hook_id}/tests".format(
            owner=owner, repo=repo, hook_id=hook_id
        )
        self.response = Response(self.post(url), "")
        if self.response.status_code == 204:
            return True
        raise ValueError(
            "test_push_hook(.....) returned {status_code}, instead it should return 204.".format(
                status_code=self.response.status_code
            )
        )

    def ping_repo_hook(self, owner, repo, hook_id):
        url = "/repos/{owner}/{repo}/hooks/{hook_id}/pings".format(
            owner=owner, repo=repo, hook_id=hook_id
        )
        self.response = Response(self.post(url), "")
        if self.response.status_code == 204:
            return True
        raise ValueError(
            "ping_hook(.....) returned {status_code}, instead it should return 204.".format(
                status_code=self.response.status_code
            )
        )

    def delete_repo_hook(self, owner, repo, hook_id):
        url = "/repos/{owner}/{repo}/hooks/{hook_id}".format(
            owner=owner, repo=repo, hook_id=hook_id
        )
        self.response = Response(self.delete(url), "")
        if self.response.status_code == 204:
            return True
        raise ValueError(
            "delete_hook(.....) returned {status_code}, instead it should return 204.".format(
                status_code=self.response.status_code
            )
        )

    # TODO: Need to implement PubSubHubbub API.
    # Subscribing  API.
