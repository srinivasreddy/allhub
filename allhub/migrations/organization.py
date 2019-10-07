from allhub.response import Response

_mime = "application/vnd.github.wyandotte-preview+json"


class OrganizationMigrationMixin:
    def start_org_migration(
        self, org, repositories, lock_repositories=False, exclude_attachments=False
    ):
        url = f"/orgs/{org}/migrations"
        params = {
            "repositories": repositories,
            "lock_repositories": lock_repositories,
            "exclude_attachments": exclude_attachments,
        }
        self.response = Response(
            self.post(url, params=params, **{"Accept": _mime}), "OrgMigration"
        )
        return self.response.transform()

    def org_migrations(self, org):
        url = f"/orgs/{org}/migrations"
        self.response = Response(self.get(url, **{"Accept": _mime}), "OrgMigrations")
        return self.response.transform()

    def org_migration_status(self, org, migration_id):
        url = f"/orgs/{org}/migrations/{migration_id}"
        self.response = Response(self.get(url, **{"Accept": _mime}), "OrgMigrations")
        return self.response.transform()

    def download_migration_archive(self, org, migration_id):
        url = f"/orgs/{org}/migrations/{migration_id}/archive"
        self.response = Response(self.get(url, **{"Accept": _mime}), "OrgMigrations")
        return self.response.transform()

    def delete_org_migration_archive(self, org, migration_id):
        url = f"/orgs/{org}/migrations/{migration_id}/archive"
        self.response = Response(self.delete(url, **{"Accept": _mime}), "OrgMigrations")
        if self.response.status_code == 204:
            return True
        raise ValueError(
            f"delete_org_migration_archive(.....) returned {self.response.status_code}, it should return 204."
        )

    def unlock_org_repository(self, org, migration_id, repo_name):
        url = f" /orgs/{org}/migrations/{migration_id}/repos/{repo_name}/lock"
        self.response = Response(self.delete(url, **{"Accept": _mime}), "OrgMigrations")
        if self.response.status_code == 204:
            return True
        raise ValueError(
            f"unlock_org_repository(.....) returned {self.response.status_code}, it should return 204."
        )
