# # library.py
# import json
# from book import Book


# class Library:
#     def _init_(self, filename='library.json'):
#         self.filename = filename
#         self.books = []
#         self.lent_books = []

#     def load_books(self):
#         try:
#             with open(self.filename, 'r') as file:
#                 data = json.load(file)
#                 self.books = [Book(**book) for book in data['books']]
#                 self.lent_books = data['lent_books']
#         except FileNotFoundError:
#             self.books = []
#             self.lent_books = []
#         except json.JSONDecodeError:
#             print("Error reading the saved file. Starting with an empty library.")
#             self.books = []
#             self.lent_books = []

#     def save_books(self):
#         try:
#             with open(self.filename, 'w') as file:
#                 data = {
#                     'books': [book._dict_ for book in self.books],
#                     'lent_books': self.lent_books
#                 }
#                 json.dump(data, file, indent=4)
#         except IOError:
#             print("Error saving the library data.")

#     def add_book(self, book):
#         self.books.append(book)
#         self.save_books()

#     def remove_book(self, isbn):
#         for book in self.books:
#             if book.isbn == isbn:
#                 self.books.remove(book)
#                 self.save_books()
#                 return
#         print("This book isn't available to remove.")

#     def view_books(self):
#         if not self.books:
#             print("No books available.")
#             return
#         for book in self.books:
#             print(book)

#     def search_books(self, term):
#         results = [book for book in self.books if term.lower(
#         ) in book.title.lower() or term in book.isbn]
#         if not results:
#             print("No books found with the given search term.")
#             return
#         for book in results:
#             print(book)

#     def search_books_by_author(self, author):
#         results = [book for book in self.books if author.lower() in (a.lower()
#                                                                      for a in book.authors)]
#         if not results:
#             print("No books found for the given author.")
#             return
#         for book in results:
#             print(book)

#     def lend_book(self, isbn, user):
#         for book in self.books:
#             if book.isbn == isbn:
#                 if book.quantity > 0:
#                     book.quantity -= 1
#                     self.lent_books.append({'isbn': isbn, 'user': user.name})
#                     self.save_books()
#                     print(f"Book lent to {user.name}.")
#                     return
#                 else:
#                     print("Not enough books available to lend.")
#                     return
#         print("Book not found.")

#     def return_book(self, isbn, user):
#         for lent_book in self.lent_books:
#             if lent_book['isbn'] == isbn and lent_book['user'] == user.name:
#                 for book in self.books:
#                     if book.isbn == isbn:
#                         book.quantity += 1
#                 self.lent_books.remove(lent_book)
#                 self.save_books()
#                 print(f"Book returned by {user.name}.")
#                 return
#         print("This book was not lent to this user.")
import json
from book import Book


class Library:
    def __init__(self, filename='library.json'):
        self.filename = filename
        self.books = []
        self.lent_books = []

    def load_books(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                self.books = [Book(**book) for book in data['books']]
                self.lent_books = data['lent_books']
        except FileNotFoundError:
            self.books = []
            self.lent_books = []
        except json.JSONDecodeError:
            print("Error reading the saved file. Starting with an empty library.")
            self.books = []
            self.lent_books = []

    def save_books(self):
        try:
            with open(self.filename, 'w') as file:
                data = {
                    'books': [book.__dict__ for book in self.books],
                    'lent_books': self.lent_books
                }
                json.dump(data, file, indent=4)
        except IOError:
            print("Error saving the library data.")

    def add_book(self, book):
        self.books.append(book)
        self.save_books()

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                self.save_books()
                return
        print("This book isn't available to remove.")

    def view_books(self):
        if not self.books:
            print("No books available.")
            return
        for book in self.books:
            print(book)

    def search_books(self, term):
        results = [book for book in self.books if term.lower(
        ) in book.title.lower() or term in book.isbn]
        if not results:
            print("No books found with the given search term.")
            return
        for book in results:
            print(book)

    def search_books_by_author(self, author):
        results = [book for book in self.books if author.lower() in (a.lower()
                                                                     for a in book.authors)]
        if not results:
            print("No books found for the given author.")
            return
        for book in results:
            print(book)

    def lend_book(self, isbn, user):
        for book in self.books:
            if book.isbn == isbn:
                if book.quantity > 0:
                    book.quantity -= 1
                    self.lent_books.append({'isbn': isbn, 'user': user.name})
                    self.save_books()
                    print(f"Book lent to {user.name}.")
                    return
                else:
                    print("Not enough books available to lend.")
                    return
        print("Book not found.")

    def return_book(self, isbn, user):
        for lent_book in self.lent_books:
            if lent_book['isbn'] == isbn and lent_book['user'] == user.name:
                for book in self.books:
                    if book.isbn == isbn:
                        book.quantity += 1
                self.lent_books.remove(lent_book)
                self.save_books()
                print(f"Book returned by {user.name}.")
                return
        print("This book was not lent to this user.")
