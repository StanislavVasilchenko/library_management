from enum import Enum


class BookStatus(Enum):
    IN_STOCK = "в наличии"
    ISSUED = "выдана"


class Book:
    """Класс Книга
    book_id: уникальный идентификатор книги
    title: название
    author: автор
    year: год издания
    status: статус (по умолчанию "в наличии")
    """

    def __init__(
        self,
        book_id: int,
        title: str,
        author: str,
        year: str,
        status: str = BookStatus.IN_STOCK.value,
    ):

        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self):
        """Получение всех полей Книги в виде словаря"""

        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status,
        }

    def __str__(self):
        return (
            f"ID: {self.book_id}, title {self.title}, "
            f"author: {self.author}, year: {self.year}, "
            f"status: {self.status}"
        )
