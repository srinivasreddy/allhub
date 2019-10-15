_mime = "application/vnd.github.antiope-preview+json"
from allhub.response import Response


class CheckRunsMixin:
    def create_check_run(
        self,
        owner,
        repo,
        name,
        head_sha,
        details_url,
        external_id,
        status,
        started_at,
        conclusion,
        completed_at,
        output,
        actions,
        **kwargs
    ):
        params = {
            "name": name,
            "head_sha": head_sha,
            "status": status,
            "external_id": external_id,
            "started_at": started_at,
            "output": output,
            "details_url": details_url,
            "conclusion": conclusion,
            "completed_at": completed_at,
            "actions": actions,
        }
        url = "/repos/{owner}/{repo}/check-runs".format(owner=owner, repo=repo)
        self.response = Response(
            self.post(url, params=params, **{"Accept": _mime}, **kwargs), "CheckRun"
        )
        return self.response.transform()

    def edit_check_run(
        self,
        owner,
        repo,
        check_run_id,
        name,
        details_url,
        external_id,
        status,
        started_at,
        conclusion,
        completed_at,
        output,
        actions,
        **kwargs
    ):
        params = {
            "name": name,
            "status": status,
            "external_id": external_id,
            "started_at": started_at,
            "output": output,
            "details_url": details_url,
            "conclusion": conclusion,
            "completed_at": completed_at,
            "actions": actions,
        }
        url = "/repos/{owner}/{repo}/check-runs/{check_run_id}".format(
            owner=owner, repo=repo, check_run_id=check_run_id
        )
        self.response = Response(
            self.patch(url, params=params, **{"Accept": _mime}, **kwargs), "CheckRun"
        )
        return self.response.transform()

    def check_runs_for_ref(
        self, owner, repo, ref, check_name, status, filter, **kwargs
    ):
        url = "/repos/{owner}/{repo}/commits/{ref}/check-runs".format(
            owner=owner, repo=repo, ref=ref
        )
        params = {"check_name": check_name, "status": status, "filter": filter}
        self.response = Response(
            self.get(url, params=params, **{"Accept": _mime}, **kwargs), "CheckRuns"
        )
        return self.response.transform()

    def check_runs_in_suite(self, owner, repo, check_suite_id, **kwargs):
        url = "/repos/{owner}/{repo}/check-suites/{check_suite_id}/check-runs".format(
            owner=owner, repo=repo, check_suite_id=check_suite_id
        )

        self.response = Response(
            self.get(url, **{"Accept": _mime}, **kwargs), "CheckSuites"
        )
        return self.response.transform()

    def single_check_run(self, owner, repo, check_run_id, **kwargs):
        url = "/repos/{owner}/{repo}/check-runs/{check_run_id}".format(
            owner=owner, repo=repo, check_run_id=check_run_id
        )
        self.response = Response(
            self.get(url, **{"Accept": _mime}, **kwargs), "CheckRun"
        )
        return self.response.transform()

    def annotations_for_check_run(self, owner, repo, check_run_id, **kwargs):
        url = "/repos/{owner}/{repo}/check-runs/{check_run_id}/annotations".format(
            owner=owner, repo=repo, check_run_id=check_run_id
        )
        self.response = Response(
            self.get(url, **{"Accept": _mime}, **kwargs), "Annotations"
        )
        return self.response.transform()
