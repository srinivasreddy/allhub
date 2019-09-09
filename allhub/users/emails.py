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
                    f"{email} should be string, but of type: {type(email)}"
                )

        c_headers = {"Accept": "application/vnd.github.giant-sentry-fist-preview+json"}
        self.response = Response(
            self.post(url, json=[("emails", emails)], **c_headers), "PublicEmails"
        )
        return self.response.transform()

    def delete_email(self, emails):
        url = "/user/emails"
        if not isinstance(emails, (list, tuple)):
            raise ValueError("The email should either be a list of strings.")
        for email in emails:
            if not isinstance(email, str):
                raise ValueError(
                    f"{email} should be string, but of type: {type(email)}"
                )

        self.response = Response(
            self.delete(
                url,
                json=[("emails", emails)],
                **{"Accept": "application/vnd.github.giant-sentry-fist-preview+json"},
            ),
            "",
        )
        return self.response.status_code == 204
