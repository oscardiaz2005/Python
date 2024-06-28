class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.borrowed = False

    def borrow(self):
        if not self.borrowed:
            self.borrowed = True
            print(f"The book '{self.title}' has been borrowed.")
        else:
            print("The book is already borrowed.")

    def return_book(self):
        if self.borrowed:
            self.borrowed = False
            print(f"The book '{self.title}' has been returned.")
        else:
            print("The book is not borrowed.")

    def search_by_author(self, author):
        return self.author.lower() == author.lower()

    def search_by_genre(self, genre):
        return self.genre.lower() == genre.lower()

    def __str__(self):
        borrow_status = "Available" if not self.borrowed else "Borrowed"
        return f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}, Status: {borrow_status}"


class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_books_by_author(self, author):
        found_books = [book for book in self.books if book.search_by_author(author)]
        return found_books

    def search_books_by_genre(self, genre):
        found_books = [book for book in self.books if book.search_by_genre(genre)]
        return found_books
