class NotOlxUrlError(Exception):
    def __init__(self, url):
        self.url = url
        self.message = f'"{url}" is not OLX url'
        super().__init__(self.message)


class NoResultFoundError(Exception):
    def __init__(self, search_request):
        self.search_request = search_request
        self.message = f'Nothing was found for "{search_request}"'
        super().__init__(self.message)


class MaxAttemptsReached(Exception):
    def __init__(self):
        self.message = f'Maximum number of retries exceeded. Error log is written to "error_logs.txt". Please provide error logs file to the developer or try to fix url'
        super().__init__(self.message)


class InvalidOlxUrl(Exception):
    def __init__(self, url):
        self.url = url
        self.message = f'"{url}" is invalid OLX url'
        super().__init__(self.message)


class InvalidAmount(Exception):
    def __init__(self, amount):
        self.amount = amount
        self.message = f'{amount} is invalid amount of products'
        super().__init__(self.message)

class AmountReached(Exception):
    def __init__(self):
        self.message = f'Needed amount of ads reached'
        super().__init__(self.message)