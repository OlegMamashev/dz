with open("input.txt", 'r') as file:
    inp = file.read()

# Преобразование содержимого файла в список
inp = inp.split()

# Количество чисел в файле (N)
kol = int(inp[0])
del inp[0]

# 1-ое число в списке
start = int(inp[0])
del inp[0]

# Результат, к которому нужно прийти (S)
out = int(inp[-1])
del inp[-1]


def find_result(numbers: int, itog: int, list1: list, numbers_now: int, result: int, stroka):
    """

    :param numbers: Количество чисел в списке
    :param itog: Результат, к которому должна прийти функция
    :param list1: Список с числами
    :param numbers_now: То, сколько чисел прошла рекурсия
    :param result: Результат выполнения рекурсии + или - (начинается с первого числа изначального списка)
    :param stroka: Строка решения рекурсии
    :return: Строка с правильной комбинацией + и -
    """

    # Проверка на правильность комбинации

    if numbers_now+1 == numbers and itog == result:
        return f"{stroka}={itog}"

    # Если использовались все возможные числа, но не пришли к результату
    elif numbers_now+1 == numbers and itog != result:
        return None

    # Плюс
    result1 = find_result(numbers, itog, list1, numbers_now+1, result+int(list1[numbers_now]),
                          f"{stroka}+{int(list1[numbers_now])}")
    if result1:
        return result1

    # Минус
    result1 = find_result(numbers, itog, list1, numbers_now+1, result-int(list1[numbers_now]),
                          f"{stroka}-{int(list1[numbers_now])}")
    if result1:
        return result1

    return result1


func = find_result(kol, out, inp, 0, start, f"{start}")

# Вывод решения в файл при наличии
if func:
    with open("output.txt", "w", encoding='utf-8') as file:
        file.write(func)
else:
    with open("output.txt", "w", encoding='utf-8') as file:
        file.write("No solution")
