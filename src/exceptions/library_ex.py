class NotChangeStatus(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class BookNotFound(Exception):
    def __init__(
        self,
        message: str = "Книга не найдена",
    ):
        self.message = message
        super().__init__(self.message)
