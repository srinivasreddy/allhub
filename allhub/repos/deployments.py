_mime = {"Accept": "application/vnd.github.ant-man-preview+json"}
from allhub.response import Response


class DeploymentMixin:
    def deployments(self, owner, repo, sha=None, ref=None, task=None, environment=None):
        url = "/repos/{owner}/{repo}/deployments".format(owner=owner, repo=repo)
        params = {}
        if sha:
            params["sha"] = sha
        if ref:
            params["ref"] = ref
        if task:
            params["task"] = task
        if environment:
            params["environment"] = environment
        self.response = Response(self.get(url, params=params, **_mime), "Deployments")
        return self.response.transform()

    def deployment(self, owner, repo, deployment_id):
        url = "/repos/{owner}/{repo}/deployments/{deployment_id}".format(
            owner=owner, repo=repo, deployment_id=deployment_id
        )
        self.response = Response(self.get(url, **_mime), "Deployments")
        return self.response.transform()

    def create_deployment(
        self,
        owner,
        repo,
        ref,
        task="deploy",
        auto_merge=True,
        required_contexts="",
        payload="",
        environment="production",
        description="",
        transient_environment=False,
        production_environment=True,
    ):
        url = "/repos/{owner}/{repo}/deployments".format(owner=owner, repo=repo)
        params = {
            "ref": ref,
            "auto_merge": auto_merge,
            "required_contexts": required_contexts,
            "task": task,
            "environment": environment,
        }
        if payload:
            params["payload"] = payload
        if description:
            params["description"] = description
        self.response = Response(self.post(url, params=params, **_mime), "Deployment")
        return self.response.transform()

    def deployment_statuses(self, owner, repo, deployment_id):
        url = "/repos/{owner}/{repo}/deployments/{deployment_id}/statuses"
        self.response = Response(self.get(url, **_mime), "DeploymentStatus")
        return self.response.transform()

    def deployment_status(self, owner, repo, deployment_id, status_id):
        url = "/repos/{owner}/{repo}/deployments/{deployment_id}/statuses/{status_id}".format(
            owner=owner, repo=repo, deployment_id=deployment_id, status_id=status_id
        )
        self.response = Response(
            self.get(url, **{"Accept": "application/vnd.github.machine-man-preview"}),
            "DeploymentStatus",
        )
        return self.response.transform()

    def create_deployment_status(
        self,
        owner,
        repo,
        deployment_id,
        state,
        environment,
        target_url="",
        log_url="",
        description="",
        environment_url="",
        auto_inactive=True,
    ):
        url = "/repos/{owner}/{repo}/deployments/{deployment_id}/statuses/".format(
            owner=owner, repo=repo, deployment_id=deployment_id
        )
        params = {
            "state": state,
            "environment": environment,
            "target_url": target_url,
            "log_url": log_url,
            "description": description,
            "environment_url": environment_url,
            "auto_inactive": auto_inactive,
        }
        self.response = Response(
            self.post(
                url,
                params=params,
                **{"Accept": "application/vnd.github.flash-preview+json"},
            ),
            "DeploymentStatus",
        )
        return self.response.transform()
