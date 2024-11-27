from src.objects.library import Library
from src.objects.books import BookStatus
from src.exceptions.library_ex import NotChangeStatus, BookNotFound


def run(library: Library):
    """Основной цикл приложения"""

    while True:
        print("\nВыберите действие:")
        print("1: Добавить книгу")
        print("2: Удалить книгу")
        print("3: Найти книгу")
        print("4: Показать все книги")
        print("5: Изменить статус книги")
        print("0: Выйти")

        action = input("Введите номер действия - ")

        match action:
            case "1":
                title = input("Введите название книги: ")
                author = input("Введите автора книги: ")
                year = input("Введите год: ")
                if year.isdigit():
                    library.add_book(title, author, year)
                    print(f"Книга {title} добавлена")
                else:
                    print(f"Год должен содержать только цифры, а вы ввели {year}")
                    continue
            case "2":
                book_id = int(input("Введите ID книги: "))
                try:
                    library.delete_book(book_id)
                    print(f"Книга с ID {book_id} удалена")
                except BookNotFound as e:
                    print(e.message)
            case "3":
                word = input("Введите название книги или автора или год: ")
                print("Найденные книги:")
                books = library.search_book(word)
                if books:
                    [print(book) for book in books]
                else:
                    print("Книг не найдено")
            case "4":
                all_books = library.display_books()
                if all_books:
                    [print(book) for book in all_books]
                else:
                    print("Библиотека пуста")
            case "5":
                search_book_id = int(input("Введите ID книги: "))
                status = input(
                    f"Введите статус книги ({' или '.join(['<' + s.value + '>' for s in BookStatus])}): "
                )
                try:
                    library.change_status(search_book_id, status)
                    print(f"У книги с ID {search_book_id} статус изменен на {status}")
                except NotChangeStatus as e:
                    print(e.message)
                except BookNotFound as e:
                    print(e.message)

            case "0":
                quit()
            case _:
                print("Вы ввели не существующее действие, повторите попытку")
