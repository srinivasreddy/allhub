from allhub.response import Response


class TeamSyncMixin:
    def idp_groups_in_org(self, org):
        url = f"/orgs/{org}/team-sync/groups"
        self.response = Response(self.get(url), "IdpGroups")
        return self.response.transform()

    def idp_groups_for_team(self, team_id):
        url = f"/teams/{team_id}/team-sync/group-mappings"
        self.response = Response(self.get(url), "IdpGroups")
        return self.response.transform()

    def create_or_update_idp_groups_connections(self, team_id, groups):
        for group in groups:
            assert "group_id" in group
            assert "group_name" in group
            assert "description" in group
        url = f"/teams/{team_id}/team-sync/group-mappings"
        self.response = Response(
            self.patch(url, params={"groups": groups}), "IdpGroupConnections"
        )
        return self.response.transform()
