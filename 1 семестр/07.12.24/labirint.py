from sys import setrecursionlimit
setrecursionlimit(9999999)


def labirint(high, width, down, left, result):
    # print(down, left, result)
    result_down = 0
    result_left = 0
    # Достигли цели
    if down == high and width == left:
        return 1
    # Выход за пределы
    if high < down or width < left:
        return 0
    # Вниз
    if down != high:
        result_down = labirint(high, width, down + 1, left, result)

    # Влево
    if left != width:
        result_left = labirint(high, width, down, left + 1, result)

    result = result_down + result_left
    return result


# Высота
n = 15

# Ширина
m = 3


print(labirint(n, m, 1, 1, 0))
