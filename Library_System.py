class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True  # True means the book is available

class Library:
    def __init__(self):
        self.books = []  # List to store books in the library

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Book added: {title} by {author}")

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Book removed: {title}")
                return
        print(f"Book not found: {title}")

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
            return
        print("Available books:")
        for idx, book in enumerate(self.books, start=1):
            status = "Available" if book.is_available else "Borrowed"
            print(f"{idx}. {book.title} by {book.author} - {status}")

    def checkout_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.is_available:
                    book.is_available = False
                    print(f"Book checked out: {title}")
                else:
                    print(f"The book '{title}' is already borrowed.")
                return
        print(f"Book not found: {title}")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if not book.is_available:
                    book.is_available = True
                    print(f"Book returned: {title}")
                else:
                    print(f"The book '{title}' was not borrowed.")
                return
        print(f"Book not found: {title}")

# Example usage
library = Library()

# Add books to the library
library.add_book("To Kill a Mockingbird", "Harper Lee")
library.add_book("1984", "George Orwell")
library.add_book("Pride and Prejudice", "Jane Austen")

# Display all books
library.display_books()

# Checkout a book
library.checkout_book("1984")

# Display books after checking out one
library.display_books()

# Return a book
library.return_book("1984")

# Display books after returning one
library.display_books()

# Remove a book from the library
library.remove_book("Pride and Prejudice")

# Display books after removing one
library.display_books()
