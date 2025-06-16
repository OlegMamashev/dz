class ListMath:
    def __init__(self, lst = None):
        if lst == None:
            self.lst_math = list()
        else:
            self.lst_math = [x for x in lst if type(x) == int or type(x) == float]
    def __add__(self, other):
        lst = [x + other for x in self.lst_math]
        return ListMath(lst)
    def __radd__(self, other):
        return self + other
    def __sub__(self, other):
        lst = [x - other for x in self.lst_math]
        return ListMath(lst)
    def __rsub__(self, other):
        lst = [other - x for x in self.lst_math]
        return ListMath(lst)
    def __mul__(self, other):
        lst = [x * other for x in self.lst_math]
        return ListMath(lst)
    def __rmul__(self, other):
        return self * other
    def __truediv__(self, other):
        lst = [x / other for x in self.lst_math]
        return ListMath(lst)
    def __rtruediv__(self, other):
        lst = [other / self for x in self.lst_math]
        return ListMath(lst)