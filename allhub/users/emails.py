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
            raise ValueError("Emails type should be list.")

        for email in emails:
            if not isinstance(email, str):
                raise ValueError("email should be string")

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
