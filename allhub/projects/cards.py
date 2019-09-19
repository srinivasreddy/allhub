from allhub.response import Response
from enum import Enum

_project_accept_header = "application/vnd.github.inertia-preview+json"


class ArchivedState(Enum):
    ALL = "all"
    ARCHIVED = "archived"
    NOT_ARCHIVED = "not_archived"


class CardsMixin:
    def project_cards(self, column_id, archived_state=ArchivedState.NOT_ARCHIVED):
        url = f"/projects/columns/{column_id}/cards"
        params = [("column_id", column_id), ("archived_state", archived_state.value)]
        self.response = Response(
            self.get(url, params=params, **{"Accept": _project_accept_header}),
            "ProjectCards",
        )
        return self.response.transform()

    def project_card(self, card_id):
        url = f"/projects/columns/cards/{card_id}"
        self.response = Response(
            self.get(url, **{"Accept": _project_accept_header}), "ProjectCard"
        )
        return self.response.transform()

    def create_project_card(self, column_id, note, content_id, content_type):
        url = f"/projects/columns/{column_id}/cards"
        params = [()]
        self.response = Response(
            self.post(url, params=params, **{"Accept": _project_accept_header}),
            "ProjectCard",
        )
        return self.response.transform()

    def update_project_card(self):
        pass

    def delete_project_card(self):
        pass

    def move_project_card(self):
        pass
