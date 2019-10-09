from allhub.response import Response


class WebHooksMixin:
    def org_hooks(self, org):
        url = f"/orgs/{org}/hooks"
        self.response = Response(self.get(url), "WebHooks")
        return self.response.transform()

    def org_hook(self, org, hook_id):
        url = f"/orgs/{org}/hooks/{hook_id}"
        self.response = Response(self.get(url), "WebHook")
        return self.response.transform()

    def create_org_hook(self, org, name, config, events=("push",), active=True):
        assert isinstance(config, dict)
        url = f"/orgs/{org}/hooks/"
        params = {
            "name": name,
            "active": active,
            "events": list(events),
            "config": config,
        }
        self.response = Response(self.post(url, params=params), "WebHook")
        return self.response.transform()

    def edit_org_hook(self, org, hook_id, config, events=("push",), active=True):
        assert isinstance(config, dict)
        url = f"/orgs/{org}/hooks/{hook_id}"
        params = {"active": active, "events": list(events), "config": config}
        self.response = Response(self.patch(url, params=params), "WebHook")
        return self.response.transform()

    def ping_org_hook(self, org, hook_id):
        url = f"/orgs/{org}/hooks/{hook_id}/pings"
        self.response = Response(self.post(url), "")
        if self.response.status_code == 204:
            return True
        raise ValueError(
            f"ping_hook(....) returned status code: {self.response.status_code}, instead of 204."
        )

    def delete_org_hook(self, org, hook_id):
        url = f"/orgs/{org}/hooks/{hook_id}"
        self.response = Response(self.delete(url), "")
        if self.response.status_code == 204:
            return True
        raise ValueError(
            f"delete_hook(....) returned status code: {self.response.status_code}, instead of 204."
        )
