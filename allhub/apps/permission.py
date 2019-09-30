from enum import Enum


class Permission(Enum):
    READ = "read"
    WRITE = "write"
    NONE = None


class AppPermission:
    def __init__(
        self,
        administration=Permission.NONE,
        blocking=Permission.NONE,
        checks=Permission.NONE,
        content_reference=Permission.NONE,
        contents=Permission.NONE,
        deployments=Permission.NONE,
        emails=Permission.NONE,
        followers=Permission.NONE,
        gpg_keys=Permission.NONE,
        issues=Permission.NONE,
        keys=Permission.NONE,
        members=Permission.NONE,
        metadata=Permission.NONE,
        organization_administration=Permission.NONE,
        organization_hooks=Permission.NONE,
        organization_plan=Permission.NONE,
        organization_projects=Permission.NONE,
        organization_user_blocking=Permission.NONE,
        packages=Permission.NONE,
        pages=Permission.NONE,
        plan=Permission.NONE,
        pull_requests=Permission.NONE,
        repository_hooks=Permission.NONE,
        repository_projects=Permission.NONE,
        single_file=Permission.NONE,
        starring=Permission.NONE,
        statuses=Permission.NONE,
        team_discussions=Permission.NONE,
        vulnerability_alerts=Permission.NONE,
        watching=Permission.NONE,
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
