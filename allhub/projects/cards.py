from allhub.response import Response
from enum import Enum

_project_accept_header = "application/vnd.github.inertia-preview+json"


class ArchivedState(Enum):
    ALL = "all"
    ARCHIVED = "archived"
    NOT_ARCHIVED = "not_archived"


class CardPosition(Enum):
    TOP = "top"
    BOTTOM = "bottom"
    AFTER = "after:{card_id}"


class CardsMixin:
    def project_cards(self, column_id, archived_state=ArchivedState.NOT_ARCHIVED):
        url = "/projects/columns/{column_id}/cards".format(column_id=column_id)
        params = {"column_id": column_id, "archived_state": archived_state.value}
        self.response = Response(
            self.get(url, params=params, **{"Accept": _project_accept_header}),
            "ProjectCards",
        )
        return self.response.transform()

    def project_card(self, card_id):
        url = "/projects/columns/cards/{card_id}".format(card_id=card_id)
        self.response = Response(
            self.get(url, **{"Accept": _project_accept_header}), "ProjectCard"
        )
        return self.response.transform()

    def create_project_card(
        self, column_id, note=None, content_id=None, content_type=None
    ):
        if note:
            if content_id is not None or content_type is not None:
                raise ValueError(
                    "When you specify note, you should not specify content_id and content_type."
                )
            params = [("note", note)]
        else:
            if content_id is None or content_type is None:
                raise ValueError(
                    "When you do not specify note, you should specify both content_id and content_type."
                )
            params = [("content_id", int(content_id)), ("content_type", content_type)]

        url = "/projects/columns/{column_id}/cards".format(column_id=column_id)
        self.response = Response(
            self.post(url, params=params, **{"Accept": _project_accept_header}),
            "ProjectCard",
        )
        return self.response.transform()

    def update_project_card(self, card_id, archived, note=None):
        params = [("archived", archived), ("note", note)]
        url = "/projects/columns/cards/{card_id}".format(card_id=card_id)
        self.response = Response(
            self.patch(url, params=params, **{"Accept": _project_accept_header}),
            "ProjectCard",
        )
        return self.response.transform()

    def delete_project_card(self, card_id):
        url = "/projects/columns/cards/{card_id}".format(card_id=card_id)
        self.response = Response(
            self.delete(url, **{"Accept": _project_accept_header}), "ProjectCard"
        )
        return self.response.status_code == 204

    def move_project_card(self, card_id, position, column_id):
        url = "/projects/columns/cards/{card_id}/moves".format(card_id=card_id)
        if position not in CardPosition:
            raise ValueError("position should be of type CardPosition.")
        params = {"position": position.value.format(card_id), "column_id": column_id}
        self.response = Response(
            self.post(url, params=params, **{"Accept": _project_accept_header}),
            "ProjectCard",
        )
        return self.response.transform()
