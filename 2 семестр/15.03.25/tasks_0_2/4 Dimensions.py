from typing import Union

class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __init__(self, a: int, b: int, c: int):
        self.__a = a
        self.__b = b
        self.__c = c
        self.dimension = a * b * c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, new):
        self.__a = new
        self.dimension = self.b * self.c * new

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, new):
        self.__b = new
        self.dimension = self.a * self.c * new

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, new):
        self.__c = new
        self.dimension = self.a * self.b * new

    def __setattr__(self, key, value):
        if key == "dimension":
            super().__setattr__(key, value)
        elif self.MIN_DIMENSION <= value and value <= self.MAX_DIMENSION:
            super().__setattr__(key, value)
        else:
            raise ValueError(f"Значение {value} не в диапазоне [{self.MIN_DIMENSION}, {self.MAX_DIMENSION}]")

    def __ge__(self, other):
        if self.dimension >= other.dimension:
            return True
        return False

    def __gt__(self, other):
        if self.dimension > other.dimension:
            return True
        return False

    def __le__(self, other):
        if self.dimension <= other.dimension:
            return True
        return False

    def __lt__(self, other):
        if self.dimension < other.dimension:
            return True
        return False


class ShopItem:
    def __init__(self, name: str, price: Union[int, float], dim: Dimensions):
        self.name = name
        self.price = price
        self.dim = dim

