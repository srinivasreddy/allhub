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
        if isinstance(emails, (list, tuple)):
            for email in emails:
                if not isinstance(email, str):
                    raise ValueError(
                        f"{email} should be string, but of type: {type(email)}"
                    )
        elif not isinstance(emails, str):
            raise ValueError("The email should either be a string or list of strings.")

        self.response = Response(
            self.post(
                url,
                payload=[("emails", emails)],
                headers={
                    "Accept": "application/vnd.github.giant-sentry-fist-preview+json"
                },
            ),
            "PublicEmails",
        )
        return self.response.transform()

    def delete_email(self, emails):
        url = "/user/emails"
        if isinstance(emails, (list, tuple)):
            for email in emails:
                if not isinstance(email, str):
                    raise ValueError("email should be string")
        elif not isinstance(emails, str):
            raise ValueError("The email should either be a string or list of strings")

        self.response = Response(
            self.delete(
                url,
                payload=[("emails", emails)],
                **{"Accept": "application/vnd.github.giant-sentry-fist-preview+json"},
            ),
            "",
        )
        return self.response.status_code == 204
