from collections import Counter
class NewList:
    __slots__ = ['list1']

    def __init__(self, a: list = []):
        self.list1 = a

    def __sub__(self, list2):
        list3 = []
        if isinstance(list2, NewList):
            dict1 = Counter((i,type(i)) for i in list2.list1)
        elif isinstance(list2, list):
            dict1 = Counter((i,type(i)) for i in list2)
        else:
            raise(TypeError("Неверный тип данных."))
        for i in self.list1:
            key = (i, type(i))
            if dict1[key]>0:
                dict1[key] -= 1
            else:
                list3.append(i)
        return NewList(list3)

list1 = NewList([1, 2, -4, 6, 10, False, True, -4, 12, 1, 1])
list2 = NewList([0, 1, 1, 2, 3, True])
list1 = list1 - list2

print(list1.list1)
