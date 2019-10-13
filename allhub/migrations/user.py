_mime = "application/vnd.github.wyandotte-preview+json"
from allhub.response import Response


class UserMigrationMixin:
    def start_user_migration(
        self, repositories, lock_repositories=False, exclude_attachments=False
    ):
        url = "/user/migrations"
        assert isinstance(repositories, (list, tuple))
        for repo in repositories:
            assert isinstance(repo, str)
        params = {"repositories": repositories, "lock_repositories": lock_repositories}
        self.response = Response(
            self.post(url, params=params, **{"Accept": _mime}), "UserMigration"
        )
        return self.response.transform()

    def user_migrations(self):
        """
        Lists all migrations a user has started.
        :return:
        """
        url = "/user/migrations"
        self.response = Response(self.get(url, **{"Accept": _mime}), "UserMigrations")
        return self.response.transform()

    def user_migration_status(self, migration_id):
        url = "/user/migrations/{migration_id}".format(migration_id=migration_id)
        self.response = Response(self.get(url, **{"Accept": _mime}), "UserMigrations")
        return self.response.transform()

    def download_user_migration_archive(self, migration_id):
        url = "/user/migrations/{migration_id}/archive".format(
            migration_id=migration_id
        )
        self.response = Response(self.get(url, **{"Accept": _mime}), "UserMigrations")
        return self.response.transform()

    def delete_user_migration_archive(self, migration_id):
        url = "/user/migrations/{migration_id}/archive".format(
            migration_id=migration_id
        )
        self.response = Response(self.delete(url, **{"Accept": _mime}), "")
        if self.response.status_code == 204:
            return True
        raise ValueError(
            "delete_user_migration_archive(......) should return 204, but it returned {status_code}".format(
                status_code=self.response.status_code
            )
        )

    def unlock_user_repository(self, migration_id, repo_name):
        url = "/user/migrations/{migration_id}/repos/{repo_name}/lock".format(
            migration_id=migration_id, repo_name=repo_name
        )
        self.response = Response(self.delete(url, **{"Accept": _mime}), "")
        if self.response.status_code == 204:
            return True
        raise ValueError(
            "unlock_user_repository(......) should return 204, but it returned {status_code}".format(
                status_code=self.response.status_code
            )
        )
