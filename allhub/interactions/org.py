from allhub.response import Response
from .util import InteractionLimit

_mime = "application/vnd.github.sombra-preview"


class OrganizationMixin:
    def org_interaction_limits(self, org):
        url = "/orgs/{org}/interaction-limits".format(org=org)
        self.response = Response(
            self.get(url, **{"Accept": _mime}), "OrgInteractionLimits"
        )
        return self.response.transform()

    def add_org_interaction_limits(self, org, limit):
        assert isinstance(limit, InteractionLimit)
        url = "/orgs/{org}/interaction-limits".format(org=org)
        self.response = Response(
            self.put(url, params={"limit": limit.value}, **{"Accept": _mime}),
            "OrgInteractionLimits",
        )
        return self.response.transform()

    def remove_org_interaction_limits(self, org):
        url = "/orgs/{org}/interaction-limits".format(org=org)
        self.response = Response(self.put(url), "")
        return self.response.status_code == 204
