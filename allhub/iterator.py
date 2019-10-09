class Iterator:
    def __init__(self, client, function, per_page, page, *args, **kwargs):
        self.client = client
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.next = True
        self.page = page
        self.per_page = per_page
        self.kwargs.update({"per_page": per_page, "page": page})

    def __iter__(self):
        return self

    def __next__(self):
        if not self.next:
            raise StopIteration()
        results = self.page_results(self.page)
        self.page += 1
        if self.client.response.next_link() is None:
            self.next = False
        return results

    def page_results(self, page=1):
        self.kwargs.update({"page": page})
        response = self.function(*self.args, **self.kwargs)
        return response
