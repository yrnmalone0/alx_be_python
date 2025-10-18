class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

# Derived class - EBook
class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

# Derived class - PrintBook
class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


#Composition - Library class
class Library:
    def __init__(self):
        self.books = []  #list to store instances of Book, EBook, and PrintBook


    def add_book(self, book):
        """Add a Book, EBook, or PrintBook instance to the library"""
        self.books.append(book)


    def list_books(self):
        """Print details of each book in the library."""
        for book in self.books:
            if isinstance(book, EBook):
                print(book)
            elif isinstance(book, PrintBook):
                print(book)
            else:
                print(book)