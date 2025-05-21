class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"title: {self.title}, author: {self.author}, pages: {self.pages}"


lst_in = ['Python', 'jk', '1024']
book = Book(lst_in[0], lst_in[1], lst_in[2])

print(book)
