_mime = "application/vnd.github.antiope-preview+json"
from allhub.response import Response


class CheckSuitesMixin:
    def check_suite(self, owner, repo, check_suite_id, **kwargs):
        url = "/repos/{owner}/{repo}/check-suites/{check_suite_id}".format(
            owner=owner, repo=repo, check_suite_id=check_suite_id
        )
        self.response = Response(
            self.get(url, **{"Accept": _mime}, **kwargs), "CheckSuite"
        )
        return self.response.transform()

    def check_suite_for_ref(self, owner, repo, ref, app_id, check_name, **kwargs):
        url = "/repos/{owner}/{repo}/{ref}/check-suites".format(
            owner=owner, repo=repo, ref=ref
        )
        params = {"app_id": app_id, "check_name": check_name}
        self.response = Response(
            self.get(url, params=params, **{"Accept": _mime}, **kwargs), "CheckSuite"
        )
        return self.response.transform()

    def set_preferences_for_check_suite(
        self, owner, repo, auto_trigger_checks, **kwargs
    ):
        url = "/repos/{owner}/{repo}/check-suites/preferences".format(
            owner=owner, repo=repo
        )
        params = {"auto_trigger_checks": auto_trigger_checks}
        self.response = Response(
            self.patch(url, params=params, **{"Accept": _mime}, **kwargs), "CheckSuite"
        )
        return self.response.transform()

    def create_check_suite(self, owner, repo, head_sha, **kwargs):
        url = "/repos/{owner}/{repo}/check-suites".format(owner=owner, repo=repo)
        self.response = Response(
            self.post(
                url, params={"head_sha": head_sha}, **{"Accept": _mime}, **kwargs
            ),
            "CheckSuite",
        )
        return self.response.transform()

    def rerequest_check_suite(self, owner, repo, check_suite_id, **kwargs):
        url = "/repos/{owner}/{repo}/check-suites/{check_suite_id}/rerequest".format(
            owner=owner, repo=repo, check_suite_id=check_suite_id
        )
        self.response = Response(
            self.post(url, **{"Accept": _mime}, **kwargs), "CheckSuite"
        )
        return self.response.transform()
