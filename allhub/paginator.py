class Paginator:
    def __init__(self, function, args, kwargs, per_page, page=1):
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.per_page = per_page
        self.page = page

    @property
    def page(self):
        self.page

    @property
    def per_page(self):
        self.per_page

    def page_results(self, page):
        return self.function(self.args, self.kwargs, self.per_page, page)
