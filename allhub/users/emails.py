from allhub.response import Response


class EmailMixin:
    def list_email(self):
        url = "/user/emails"
        self.response = Response(
            self.get(
                url,
                **{"Accept": "application/vnd.github.giant-sentry-fist-preview+json"},
            ),
            "Emails",
        )
        return self.response.transform()

    def list_public_email(self):
        url = "/user/public_emails"
        self.response = Response(
            self.get(
                url,
                **{"Accept": "application/vnd.github.giant-sentry-fist-preview+json"},
            ),
            "PublicEmails",
        )
        return self.response.transform()

    def add_email(self, emails):
        url = "/user/emails"
        if not isinstance(emails, (list, tuple)):
            raise ValueError("The email should either be a list of strings.")
        for email in emails:
            if not isinstance(email, str):
                raise ValueError(
                    "{email} should be string, but of type: {type}".format(
                        email=email, type=type(email)
                    )
                )

        c_headers = {"Accept": "application/vnd.github.giant-sentry-fist-preview+json"}
        self.response = Response(
            self.post(url, params=[("emails", emails)], **c_headers), "PublicEmails"
        )
        return self.response.transform()

    def delete_email(self, emails):
        url = "/user/emails"
        if not isinstance(emails, (list, tuple)):
            raise ValueError("The email should either be a list of strings.")
        for email in emails:
            if not isinstance(email, str):
                raise ValueError(
                    "{email} should be string, but of type: {type}".format(
                        email=email, type=type(email)
                    )
                )

        self.response = Response(
            self.delete(
                url,
                params=[("emails", emails)],
                **{"Accept": "application/vnd.github.giant-sentry-fist-preview+json"},
            ),
            "",
        )
        if self.response.status_code == 204:
            return True
        elif self.response.status_code == 404:
            return False
        else:
            raise ValueError(
                "the API returned response code:{status_code}, it should either be 204 or 404".format(
                    status_code=self.response.status_code
                )
            )

    def toggle_email_visibility(self, email, visibility):
        url = "/user/email/visibility"
        if visibility not in ("public", "private"):
            raise ValueError("visibility should either be public or private.")
        self.response = Response(
            self.patch(
                url,
                params=[("email", email), ("visibility", visibility)],
                **{"Accept": "application/vnd.github.giant-sentry-fist-preview+json"},
            ),
            "EmailVisibility",
        )
        return self.response.transform()
