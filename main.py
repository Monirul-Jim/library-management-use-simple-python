# # main.py
# from library import Library
# from book import Book
# from user import User
# from utils import get_float_input, get_int_input


# def main():
#     library = Library()
#     library.load_books()

#     while True:
#         print("\nLibrary Management System")
#         print("1. Add Book")
#         print("2. View All Books")
#         print("3. Search Books")
#         print("4. Search Books by Author")
#         print("5. Remove Book")
#         print("6. Lend Book")
#         print("7. Return Book")
#         print("8. View Lent Books")
#         print("9. Exit")

#         choice = input("Enter your choice: ")

#         if choice == '1':
#             title = input("Enter book title: ")
#             authors = input("Enter authors (comma separated): ").split(',')
#             isbn = input("Enter ISBN: ")
#             year = get_int_input("Enter publishing year: ")
#             price = get_float_input("Enter price: ")
#             quantity = get_int_input("Enter quantity: ")

#             book = Book(title, authors, isbn, year, price, quantity)
#             library.add_book(book)
#             print("Book added successfully.")

#         elif choice == '2':
#             library.view_books()

#         elif choice == '3':
#             term = input("Enter search term (title or ISBN): ")
#             library.search_books(term)

#         elif choice == '4':
#             author = input("Enter author name: ")
#             library.search_books_by_author(author)

#         elif choice == '5':
#             isbn = input("Enter ISBN of the book to remove: ")
#             library.remove_book(isbn)

#         elif choice == '6':
#             isbn = input("Enter ISBN of the book to lend: ")
#             user_name = input("Enter user name: ")
#             user = User(user_name)
#             library.lend_book(isbn, user)

#         elif choice == '7':
#             isbn = input("Enter ISBN of the book to return: ")
#             user_name = input("Enter user name: ")
#             user = User(user_name)
#             library.return_book(isbn, user)

#         elif choice == '8':
#             print("Lent Books:")
#             if not library.lent_books:
#                 print("No books currently lent out.")
#             for lent_book in library.lent_books:
#                 print(f"ISBN: {lent_book['isbn']}, User: {lent_book['user']}")

#         elif choice == '9':
#             break

#         else:
#             print("Invalid choice. Please try again.")


# if __name__ == "__main__":
#     main()
from library import Library
from book import Book
from user import User
from utils import get_float_input, get_int_input


def main():
    library = Library()
    library.load_books()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Books")
        print("4. Search Books by Author")
        print("5. Remove Book")
        print("6. Lend Book")
        print("7. Return Book")
        print("8. View Lent Books")
        print("9. Exit")

        try:
            choice = input("Enter your choice: ")
        except KeyboardInterrupt:
            print("\nYou Quite the program.")
            break

        if choice == '1':
            title = input("Enter book title: ")
            authors = input("Enter authors (comma separated): ").split(',')
            isbn = input("Enter ISBN: ")
            year = get_int_input("Enter publishing year: ")
            price = get_float_input("Enter price: ")
            quantity = get_int_input("Enter quantity: ")

            book = Book(title, authors, isbn, year, price, quantity)
            library.add_book(book)
            print("Book added successfully.")

        elif choice == '2':
            library.view_books()

        elif choice == '3':
            term = input("Enter search term (title or ISBN): ")
            library.search_books(term)

        elif choice == '4':
            author = input("Enter author name: ")
            library.search_books_by_author(author)

        elif choice == '5':
            isbn = input("Enter ISBN of the book to remove: ")
            library.remove_book(isbn)

        elif choice == '6':
            isbn = input("Enter ISBN of the book to lend: ")
            user_name = input("Enter user name: ")
            user = User(user_name)
            library.lend_book(isbn, user)

        elif choice == '7':
            isbn = input("Enter ISBN of the book to return: ")
            user_name = input("Enter user name: ")
            user = User(user_name)
            library.return_book(isbn, user)

        elif choice == '8':
            print("Lent Books:")
            if not library.lent_books:
                print("No books currently lent out.")
            for lent_book in library.lent_books:
                print(f"ISBN: {lent_book['isbn']}, User: {lent_book['user']}")

        elif choice == '9':
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
