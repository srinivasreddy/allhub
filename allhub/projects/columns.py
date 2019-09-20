from allhub.response import Response
from enum import Enum

_project_accept_header = "application/vnd.github.inertia-preview+json"


class CardPosition(Enum):
    TOP = "top"
    BOTTOM = "bottom"
    AFTER = "after:{card_id}"


class ColumnsMixin:
    def project_columns(self, project_id):
        url = f"/projects/{project_id}/columns"
        self.response = Response(
            self.get(url, **{"Accept": _project_accept_header}), "Columns"
        )

        return self.response.transform()

    def project_column(self, column_id):
        url = f"/projects/columns/{column_id}"
        self.response = Response(
            self.get(url, **{"Accept": _project_accept_header}), "Column"
        )

        return self.response.transform()

    def create_project_column(self, project_id, name):
        url = f"/projects/{project_id}/columns"
        params = [("name", name)]
        self.response = Response(
            self.post(url, params=params, **{"Accept": _project_accept_header}),
            "Column",
        )

        return self.response.transform()

    def update_project_column(self, column_id, name):
        url = f"/projects/columns/{column_id}"
        params = [("name", name)]
        self.response = Response(
            self.patch(url, params=params, **{"Accept": _project_accept_header}),
            "Column",
        )

        return self.response.transform()

    def delete_project_column(self, column_id):
        url = f"/projects/columns/{column_id}"
        self.response = Response(
            self.delete(url, **{"Accept": _project_accept_header}), "Column"
        )

        return self.response.status_code == 204

    def move_project_column(self, column_id, position):
        url = f"/projects/columns/{column_id}/moves"
        if position not in CardPosition:
            raise ValueError("position should be of type CardPosition.")
        params = [("position", position.value)]
        self.response = Response(
            self.post(url, params=params, **{"Accept": _project_accept_header}),
            "Column",
        )

        return self.response.transform()
