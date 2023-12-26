import json
from book import Book
from book_iterator import BookIterator


class BookStore:
    def __init__(self, books=[]):
        self.books = books

    def add_book(self, title, author, category, release_date):
        new_book = Book(title, author, category, release_date)
        self.books.append(new_book)

    def save_books_to_file(self, filename):
        with open(filename, 'w') as file:
            books_data = [{'title': book.title, 'author': book.author, 'category': book.category, 'release_date': book.release_date.strftime('%Y-%m-%d')} for book in self.books]
            json.dump(books_data, file)

    def load_books_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                data = file.read()
                if data:  # Check if the file is not empty
                    books_data = json.loads(data)
                    self.books = [Book(**book_data) for book_data in books_data]
                else:
                    print("The file is empty. No data to load.")
        except FileNotFoundError:
            print("File not found. Creating a new one.")
        except json.decoder.JSONDecodeError:
            print("Error decoding JSON. Make sure the file has a correct format.")

    def get_books_iterator(self):
        return BookIterator(sorted(self.books, key=lambda x: x.release_date, reverse=True))

    def get_author_books_iterator(self, author):
        author_books = [book for book in self.books if book.author == author]
        return BookIterator(sorted(author_books, key=lambda x: x.release_date, reverse=True))

    def get_category_books_iterator(self, category):
        category_books = [book for book in self.books if book.category == category]
        return BookIterator(sorted(category_books, key=lambda x: x.release_date, reverse=True))

    def get_recommendations_for_book(self, book):
        recommendations = [b for b in self.books if b.category == book.category and b != book]
        return BookIterator(sorted(recommendations, key=lambda x: x.release_date, reverse=True))