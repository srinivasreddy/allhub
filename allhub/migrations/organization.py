from allhub.response import Response

_mime = "application/vnd.github.wyandotte-preview+json"


class OrganizationMigrationMixin:
    def start_org_migration(
        self, org, repositories, lock_repositories=False, exclude_attachments=False
    ):
        url = "/orgs/{org}/migrations".format(org=org)
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
        url = "/orgs/{org}/migrations".format(org=org)
        self.response = Response(self.get(url, **{"Accept": _mime}), "OrgMigrations")
        return self.response.transform()

    def org_migration_status(self, org, migration_id):
        url = "/orgs/{org}/migrations/{migration_id}".format(
            org=org, migration_id=migration_id
        )
        self.response = Response(self.get(url, **{"Accept": _mime}), "OrgMigrations")
        return self.response.transform()

    def download_migration_archive(self, org, migration_id):
        url = "/orgs/{org}/migrations/{migration_id}/archive".format(
            org=org, migration_id=migration_id
        )
        self.response = Response(self.get(url, **{"Accept": _mime}), "OrgMigrations")
        return self.response.transform()

    def delete_org_migration_archive(self, org, migration_id):
        url = "/orgs/{org}/migrations/{migration_id}/archive".format(
            org=org, migration_id=migration_id
        )
        self.response = Response(self.delete(url, **{"Accept": _mime}), "OrgMigrations")
        if self.response.status_code == 204:
            return True
        raise ValueError(
            "delete_org_migration_archive(.....) returned {status_code}, it should return 204.".format(
                status_code=self.response.status_code
            )
        )

    def unlock_org_repository(self, org, migration_id, repo_name):
        url = "/orgs/{org}/migrations/{migration_id}/repos/{repo_name}/lock".format(
            org=org, migration_id=migration_id, repo_name=repo_name
        )
        self.response = Response(self.delete(url, **{"Accept": _mime}), "OrgMigrations")
        if self.response.status_code == 204:
            return True
        raise ValueError(
            "unlock_org_repository(.....) returned {status_code}, it should return 204.".format(
                status_code=self.response.status_code
            )
        )
