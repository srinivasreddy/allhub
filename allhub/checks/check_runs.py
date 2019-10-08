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
        url = f"/repos/{owner}/{repo}/check-runs"
        self.response = Response(
            self.post(url, params=params, **{"Accept": _mime}), "CheckRun"
        )
        return self.response.transform()
