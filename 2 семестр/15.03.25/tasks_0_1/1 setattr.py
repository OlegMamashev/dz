class Book:
    def __init__(self, title_, author_, pages_, year_):
        self.title = title_
        self.author = author_
        self.pages = pages_
        self.year = year_
    
    def __str__(self):
        return f"title: {self.title}, author: {self.author}, pages: {self.pages}, year: {self.year}"
    
    def __setattr__(self, name, value):
        if name == 'title' or name == 'author':
            if isinstance(value, str):
                self.__dict__[name] = value
            else:
                raise TypeError("Неверный тип присваиваемых данных.")
        if name == 'pages' or name == 'year':
            if  isinstance(value, int):
                self.__dict__[name] = value
            else:
                raise TypeError("Неверный тип присваиваемых данных.")
            
        # super().__setattr__(name,value) - правильный способ добавления аттрибутов

book = Book('Jk', 'OOP', 123, 2022)
print(book.__dict__)
print(str(book))

