from tests.utils import allhub


class TestPullRequests:
    def test_pull_requests_in_repo(self):
        response = allhub.repo_pull_requests("python", "cpython")
        assert response[0].body is not None
        assert len(response) == 30

    def test_pull_requests_in_repo_with_page_per_page_params(self):
        response = allhub.repo_pull_requests("python", "cpython", page=4, per_page=50)
        assert response[0].body is not None
        assert len(response) == 50

    def test_pull_request_in_repo(self):
        response = allhub.repo_pull_request("python", "cpython", 16716)
        assert response.body is not None
        assert response.user.login == "goswami-rahul"

    def test_create_pull_request(self):
        pass

    def test_update_pull_request_branch(self):
        pass

    def test_update_pull_request(self):
        pass

    def test_commits_in_pull_request(self):
        response = allhub.commits_in_pull_request(
            "python", "cpython", 9916
        )  # 9916 is the PR i have created.
        assert len(response) == 3
        assert response[0].commit.author.name == "Srinivas Reddy Thatiparthy"
        assert response[1].commit.author.name == "Srinivas Reddy Thatiparthy"
        assert response[2].commit.author.name == "Srinivas Reddy Thatiparthy"

        sorted(
            [
                "71d9896a10524a9e1265fc5aa058edcad6e9d59a",
                "ff6060c6d2838acf09e3a0519104a920aadf924a",
                "bf08bac13cc759666b0fbbbfa153a14a18b83eda",
            ]
        ) == sorted([resp.sha for resp in response])

    def test_files_in_pull_request(self):
        # 9916 is the PR i have created.
        response = allhub.files_in_pull_request("python", "cpython", 9916)
        sorted(
            [
                "Misc/NEWS.d/next/Library/2018-10-17-02-15-23.bpo-33947.SRuq3T.rst",
                "Lib/test/test_dataclasses.py",
                "Lib/dataclasses.py",
            ]
        ) == sorted([resp.filename for resp in response])

    def test_is_pull_request_has_been_merged(self):
        assert allhub.is_pull_request_has_been_merged(
            "python", "cpython", 9916
        )  # Merged successfully.
        assert not allhub.is_pull_request_has_been_merged(
            "python", "cpython", 10564
        )  # PR has been closed.

    def test_merge_pull_request(self):
        pass
