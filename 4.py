class Product:
    pass


class Book(Product):
    def __init__(self, name, author, pages, price):
        self.name = name
        self.author = author
        self.pages = pages
        self.price = price

    def get_book(self):
        return f'Название книги: {self.name}\n' \
               f'Автор: {self.author}\n' \
               f'Колличество страниц: {self.pages}\n' \
               f'Стоимость: {self.price}'


capital = Book('Капитал', 'Карл Маркс', 100500, 100500.00)
aspid = Book('Аспид', 'Кристина Старк', 480, 19.56)
cinderella = Book('Золушка', 'Марисса Мейер', 416, 17.99)

# print(aspid.get_book())
