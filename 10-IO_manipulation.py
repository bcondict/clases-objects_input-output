# Write your class definition here
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def decribe_book(self):
        print(f"Title: [{self.title}], Author: [{self.author}]")


title = input("Enter the title of the book: ")
author = input("Enter the author of the book: ")

# Create an instance of Book here
book = Book(title, author)
book.decribe_book()
