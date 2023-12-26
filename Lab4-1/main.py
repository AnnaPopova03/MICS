from book_store import BookStore
from book_iterator import BookIterator
from book import Book


def display_books(iterator, title): # Function to display books
    print(f"\n{title}:")
    for book in iterator:
        print(f"- {book}")


def main(): 
    # Try to load books from the file first
    book_store = BookStore()
    book_store.load_books_from_file('books_data.json')
    # Console interface
    while True:
        print("\n===== Book Online Store =====")
        print("1. Add a book")
        print("2. View all books")
        print("3. View books by author")
        print("4. View books by category")
        print("5. Display recommendations for a selected book")
        print("0. Exit")

        ch = input("Choose an option: ")

        if ch == "1":
            title = input("Enter the book title: ")
            author = input("Enter the book author: ")
            category = input("Enter the book category: ")
            release_date = input("Enter the book release date (year-month-day): ")
            book_store.add_book(title, author, category, release_date)
            print("Book added successfully!")

        elif ch == "2":
            all_books_iterator = book_store.get_books_iterator()
            display_books(all_books_iterator, "All Books")

        elif ch == "3":
            author_name = input("Enter the author's name: ")
            author_books_iterator = book_store.get_author_books_iterator(author_name)
            display_books(author_books_iterator, f"Books by {author_name}")

        elif ch == "4":
            category_name = input("Enter the category: ")
            category_books_iterator = book_store.get_category_books_iterator(category_name)
            display_books(category_books_iterator, f"Books in category {category_name}")

        elif ch == "5":
            selected_book = select_book(book_store.get_books_iterator())
            if selected_book:
                print("\nSelected book:", selected_book)
                # Display recommendations
                recommendations_iterator = book_store.get_recommendations_for_book(selected_book)
                display_books(recommendations_iterator, "Recommendations for the selected book")

        elif ch == "0":
            print("Thank you for using our store. Goodbye!")
            # Save books to the file when exiting the program
            book_store.save_books_to_file('books_data.json')
            break

        else:
            print("Invalid choice. Please enter a valid option.")

def select_book(iterator):
    try:
        index = int(input("Enter the book number: "))
        selected_book = None
        for i, book in enumerate(iterator):
            if i == index:
                selected_book = book
                break
        if selected_book is None:
            print("Book with the specified number not found.")
        return selected_book
    except ValueError:
        print("Please enter a valid book number.")
        return None

if __name__ == "__main__":
    main()