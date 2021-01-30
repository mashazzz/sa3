# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
"""

class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def bookInfo(self):
        print("Book title:", self.title)
        print("Book author:", self.author,"\n")

b1 = Book("Software Requirements", "Wiegers, Karl")
b2 = Book("Writing Effective Use Cases", "Cockburn, Alistair")
b3 = Book("The Elements of UML 2.0 Style", "Ambler, Scott")


bookshelf = [b1, b2, b3]

for book in bookshelf:
    book.bookInfo()

print ("Number of books: " + str(len(bookshelf)))