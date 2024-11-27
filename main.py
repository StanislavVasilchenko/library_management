from src.objects.library import Library
from src import main_loop


if __name__ == "__main__":
    library = Library()
    main_loop.run(library)

