from allhub.response import Response
from allhub.util import MediaType


class GitIgnoreMixin:
    def git_ignore_templates(self):
        # TODO: This API is returning [None, ..........None]
        # Not sure this API is working anymore.
        url = "/gitignore/templates"
        self.response = Response(self.get(url), "Templates")
        return self.response.transform()

    def git_ignore_template(self, name, media_type=MediaType.JSON):
        url = "/gitignore/templates/{name}".format(name=name)
        self.response = Response(
            self.get(url, **{"Accept": media_type.value}), "Template"
        )
        return self.response.transform()
