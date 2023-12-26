class BookIterator:
    def __init__(self, books):
        self.books = books

    def __iter__(self):
        return self

    def __next__(self):
        if self.books:
            current_book = self.books.pop(0)
            return current_book
        else:
            raise StopIteration