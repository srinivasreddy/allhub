from allhub.response import Response
from enum import Enum


class MilestoneSort(Enum):
    DUE_ON = "due_on"
    COMPLETENESS = "completeness"


class MilestoneState(Enum):
    OPEN = "open"
    CLOSED = "closed"
    ALL = "all"


class MilestoneDirection(Enum):
    ASC = "asc"
    DSC = "DSC"


class MilestoneMixin:
    def milestones(
        self,
        owner,
        repo,
        state=MilestoneState.OPEN,
        sort=MilestoneSort.DUE_ON,
        direction=MilestoneDirection.ASC,
    ):
        url = "/repos/{owner}/{repo}/milestones".format(owner=owner, repo=repo)
        params = {
            "state": state.value,
            "sort": sort.value,
            "direction": direction.value,
        }
        self.response = Response(self.get(url, params=params), "Milestones")
        return self.response.transform()

    def milestone(self, owner, repo, milestone_number):
        url = "/repos/{owner}/{repo}/milestones/{milestone_number}".format(
            owner=owner, repo=repo, milestone_number=milestone_number
        )
        self.response = Response(self.get(url), "Milestone")
        return self.response.transform()

    def create_milestone(self, owner, repo, title, state, description, due_on):
        url = "/repos/{owner}/{repo}/milestones".format(owner=owner, repo=repo)
        params = {
            "title": title,
            "state": state,
            "description": description,
            "due_on": due_on,
        }
        self.response = Response(self.post(url, params=params), "Milestone")
        return self.response.transform()

    def update_milestone(
        self, owner, repo, milestone_number, title, state, description, due_on
    ):
        url = "/repos/{owner}/{repo}/milestones/{milestone_number}".format(
            owner=owner, repo=repo, milestone_number=milestone_number
        )
        params = {
            "title": title,
            "state": state,
            "description": description,
            "due_on": due_on,
        }
        self.response = Response(self.patch(url, param=params), "Milestone")
        return self.response.transform()

    def delete_milestone(self, owner, repo, milestone_number):
        url = "/repos/{owner}/{repo}/milestones/{milestone_number}".format(
            owner=owner, repo=repo, milestone_number=milestone_number
        )
        self.response = Response(self.delete(url), "")
        return self.response.status_code == 204
