import json
import os
from typing import List

from src.objects.books import Book, BookStatus
from src.utils import gen_next_book_id, get_book
from src.exceptions.library_ex import NotChangeStatus, BookNotFound


class Library:
    """Класс Библиотнеки
    books: список всех книг находящихся в библиотеке
    data_file_name: имя файла json для хранения книг, по умолчанию data.json
    """

    def __init__(self, data_file_name="data.json"):
        self.books = []
        self.data_file_name = data_file_name
        self.load_book()
        if self.books:
            self.book_id = gen_next_book_id(self.books[-1].book_id)
        else:
            self.book_id = gen_next_book_id()

    def load_book(self):
        """Если файл с ранее созданными книгами существует, то при запуске приложения
        он прочтется и все книги будут доступны в books."""

        if os.path.exists(self.data_file_name):
            with open(self.data_file_name, "r", encoding="utf-8") as file:
                self.books = [Book(**book) for book in json.load(file)]

    def save_book(self):
        """Сохранение книг в файл"""

        with open(self.data_file_name, "w", encoding="utf-8") as file:
            json.dump(
                [book.to_dict() for book in self.books],
                file,
                indent=4,
                ensure_ascii=False,
            )

    def add_book(self, title: str, author: str, year: str) -> None:
        """Добавление книги в библиотку"""

        book = Book(
            book_id=next(self.book_id),
            title=title,
            author=author,
            year=year,
        )
        self.books.append(book)
        self.save_book()

    def delete_book(self, book_id: int) -> Book | None:
        """Удаление книги из библиотеки"""

        book = get_book(book_id, self.books)
        if book:
            self.books.remove(book)
            self.save_book()
            return book
        raise BookNotFound()

    def search_book(self, search_word: str) -> List[Book]:
        """Поиск книги по названию/имени автора/году издания"""

        found_books = [
            book
            for book in self.books
            if search_word.lower()
            in (book.title.lower(), book.author.lower(), book.year)
        ]
        return found_books

    def display_books(self) -> List[Book]:
        """Отображение всех книг находящихся в библиотеке"""

        return self.books

    def change_status(self, book_id, new_status):
        """Изменения статуса книги по ID"""

        if new_status in BookStatus:
            book = get_book(book_id, self.books)
            if book:
                book.status = new_status
                self.save_book()
            else:
                raise BookNotFound(f"Книги с ID {book_id} не найденно")
        else:
            raise NotChangeStatus(
                f"Не возможно присвоить статус - {new_status},"
                f" выберите {' или '.join(['<' + status.value + '>' for status in BookStatus])}"
            )
