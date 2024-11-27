from src.objects.books import Book


def gen_next_book_id(next_id: int = 0):
    """Генерирует следующий ID книги"""

    count = next_id + 1
    while True:
        yield count
        count += 1


def get_book(book_id: int, library_data: list) -> Book | bool:
    """Получение одной книги по ID из всей библиотеки"""

    start = 0
    end = len(library_data) - 1
    mid = len(library_data) // 2

    while start <= end:
        if book_id == library_data[mid].book_id:
            return library_data[mid]
        if book_id < library_data[mid].book_id:
            end = mid - 1
            mid = (start + end) // 2
        elif book_id > library_data[mid].book_id:
            start = mid + 1
            mid = (start + end) // 2
    return False
