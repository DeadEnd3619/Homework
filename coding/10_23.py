class Book():
    def __init__(self, title, author, isbn,):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.position = 'Checked in'
    def __str__(self):
        print(f"The title of the book is {self.title} and the author is {self.author}. The book is {self.position} and the ISBN number is {self.isbn}")
    def borrowing(self):
        