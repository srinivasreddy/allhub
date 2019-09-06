class Iterator:
    def __init__(self, user, function, page, per_page, args, kwargs):
        self.user = user
        self.page = page
        self.per_page = per_page
        self.function = function
        self.args = args
        self.kwargs = kwargs

    def __iter__(self):
        return self

    def __next__(self):
        result = self.function(*self.args, **self.kwargs)
        return result
