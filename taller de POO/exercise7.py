from clases.clase_exercise7 import *

book_manager = BookManager()
book1 = Book("One Hundred Years of Solitude", "Gabriel Garcia Marquez", "Magical Realism")
book2 = Book("Don Quixote", "Miguel de Cervantes", "Novel")
book3 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "Fantasy")
book4 = Book("Chronicle of a Death Foretold", "Gabriel Garcia Marquez", "Magical Realism")
book_manager.add_book(book1)
book_manager.add_book(book2)
book_manager.add_book(book3)
book_manager.add_book(book4)

def show_menu():
    print("\nMenu:")
    print("1. Borrow book")
    print("2. Return book")
    print("3. Search books by author")
    print("4. Search books by genre")
    print("5. Show all books")
    print("6. Exit")

while True:
    show_menu()
    option = input("Select an option: ")

    if option == "1":
        title = input("Enter the title of the book to borrow: ")
        for book in book_manager.books:
            if book.title.lower() == title.lower():
                book.borrow()
                break
        else:
            print("The book is not in the library.")
    elif option == "2":
        title = input("Enter the title of the book to return: ")
        for book in book_manager.books:
            if book.title.lower() == title.lower():
                book.return_book()
                break
        else:
            print("The book is not in the library.")
    elif option == "3":
        author = input("Enter the author's name to search for books: ")
        print(f"Books by {author}:")
        found_books = book_manager.search_books_by_author(author)
        if found_books:
            for book in found_books:
                print(book)
        else:
            print("No books found by that author.")
    elif option == "4":
        genre = input("Enter the genre to search for books: ")
        print(f"Books in the genre {genre}:")
        found_books = book_manager.search_books_by_genre(genre)
        if found_books:
            for book in found_books:
                print(book)
        else:
            print("No books found in that genre.")
    elif option == "5":
        print("All books:")
        for book in book_manager.books:
            print(book)
    elif option == "6":
        print("Thank you for using the library. Goodbye!")
        break
    else:
        print("Invalid option. Please select a valid option.")
