# Write your class definition here
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def decribe_book(self):
        print(f"Title: [{self.title}], Author: [{self.author}]")


# Create an instance of Book here
book = Book("Python Basics", "John Doe")
book.decribe_book()

