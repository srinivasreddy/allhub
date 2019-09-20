from enum import Enum


class Permission(Enum):
    READ = "read"
    WRITE = "write"


class AppPermission:
    def __init__(self):
        self.administration = None
        self.blocking = None
        self.checks = None
        self.content_reference = None
        self.contents = None
        self.deployments = None
        self.emails = None
        self.followers = None
        self.gpg_keys = None
        self.issues = None
        self.keys = None
        self.members = None
        self.metadata = None
        self.organization_administration = None
        self.organization_hooks = None
        self.organization_plan = None
        self.organization_projects = None
        self.organization_user_blocking = None
        self.packages = None
        self.pages = None
        self.plan = None
        self.pull_requests = None
        self.repository_hooks = None
        self.repository_projects = None
        self.single_file = None
        self.starring = None
        self.statuses = None
        self.team_discussions = None
        self.vulnerability_alerts = None
        self.watching = None

    def administration(self, permission):
        self.administration = permission.value
        return self

    def blocking(self, permission):
        self.blocking = permission.value
        return self

    def checks(self, permission):
        self.checks = permission.value
        return self

    def content_reference(self, permission):
        self.content_reference = permission.value
        return self

    def contents(self, permission):
        self.contents = permission.value
        return self

    def deployments(self, permission):
        self.deployments = permission.value
        return self

    def emails(self, permission):
        self.emails = permission.value
        return self

    def followers(self, permission):
        self.followers = permission.value
        return self

    def gpg_keys(self, permission):
        self.gpg_keys = permission.value
        return self

    def issues(self, permission):
        self.issues = permission.value
        return self

    def keys(self, permission):
        self.keys = permission.value
        return self

    def members(self, permission):
        self.members = permission.value
        return self

    def metadata(self, permission):
        self.metadata = permission.value
        return self

    def organization_administration(self, permission):
        self.organization_administration = permission.value
        return self

    def organization_hooks(self, permission):
        self.organization_hooks = permission.value
        return self

    def organization_plan(self, permission):
        self.organization_plan = permission.value
        return self

    def organization_projects(self, permission):
        self.organization_projects = permission.value
        return self

    def organization_user_blocking(self, permission):
        self.organization_user_blocking = permission.value
        return self

    def packages(self, permission):
        self.packages = permission.value
        return self

    def pages(self, permission):
        self.pages = permission.value
        return self

    def plan(self, permission):
        self.plan = permission.value
        return self

    def pull_requests(self, permission):
        self.pull_requests = permission.value
        return self

    def repository_hooks(self, permission):
        self.repository_hooks = permission.value
        return self

    def repository_projects(self, permission):
        self.repository_projects = permission.value
        return self

    def single_file(self, permission):
        self.single_file = permission.value
        return self

    def starring(self, permission):
        self.starring = permission.value
        return self

    def statuses(self, permission):
        self.statuses = permission.value
        return self

    def team_discussions(self, permission):
        self.team_discussions = permission.value
        return self

    def vulnerability_alerts(self, permission):
        self.vulnerability_alerts = permission.value
        return self

    def watching(self, permission):
        self.watching = permission.value
        return self

    def to_dict(self):
        return {
            attr: getattr(self, attr) for attr in dir(self) if not attr.startswith("__")
        }
