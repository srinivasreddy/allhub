from enum import Enum


# TODO: Need to check again how these names fare while using API.


class AppPermissionEnum(Enum):
    READ = "read"
    WRITE = "write"
    NONE = None


class AppPermission:
    def __init__(
        self,
        administration=AppPermissionEnum.NONE,
        blocking=AppPermissionEnum.NONE,
        checks=AppPermissionEnum.NONE,
        content_reference=AppPermissionEnum.NONE,
        contents=AppPermissionEnum.NONE,
        deployments=AppPermissionEnum.NONE,
        emails=AppPermissionEnum.NONE,
        followers=AppPermissionEnum.NONE,
        gpg_keys=AppPermissionEnum.NONE,
        issues=AppPermissionEnum.NONE,
        keys=AppPermissionEnum.NONE,
        members=AppPermissionEnum.NONE,
        metadata=AppPermissionEnum.NONE,
        organization_administration=AppPermissionEnum.NONE,
        organization_hooks=AppPermissionEnum.NONE,
        organization_plan=AppPermissionEnum.NONE,
        organization_projects=AppPermissionEnum.NONE,
        organization_user_blocking=AppPermissionEnum.NONE,
        packages=AppPermissionEnum.NONE,
        pages=AppPermissionEnum.NONE,
        plan=AppPermissionEnum.NONE,
        pull_requests=AppPermissionEnum.NONE,
        repository_hooks=AppPermissionEnum.NONE,
        repository_projects=AppPermissionEnum.NONE,
        single_file=AppPermissionEnum.NONE,
        starring=AppPermissionEnum.NONE,
        statuses=AppPermissionEnum.NONE,
        team_discussions=AppPermissionEnum.NONE,
        vulnerability_alerts=AppPermissionEnum.NONE,
        watching=AppPermissionEnum.NONE,
    ):

        self.administration = administration
        self.blocking = blocking
        self.checks = checks
        self.content_reference = content_reference
        self.contents = contents
        self.deployments = deployments
        self.emails = emails
        self.followers = followers
        self.gpg_keys = gpg_keys
        self.issues = issues
        self.keys = keys
        self.members = members
        self.metadata = metadata
        self.organization_administration = organization_administration
        self.organization_hooks = organization_hooks
        self.organization_plan = organization_plan
        self.organization_projects = organization_projects
        self.organization_user_blocking = organization_user_blocking
        self.packages = packages
        self.pages = pages
        self.plan = plan
        self.pull_requests = pull_requests
        self.repository_hooks = repository_hooks
        self.repository_projects = repository_projects
        self.single_file = single_file
        self.starring = starring
        self.statuses = statuses
        self.team_discussions = team_discussions
        self.vulnerability_alerts = vulnerability_alerts
        self.watching = watching

    def to_dict(self):
        return {
            attr: getattr(self, attr).value
            for attr in dir(self)
            if not attr.startswith("__") and getattr(self, attr).value is not None
        }
