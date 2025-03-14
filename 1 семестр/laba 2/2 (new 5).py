def movements(size: int, down: int, right: int) -> list:
    """
    Функция принимает координаты вниз - влево и возвращает координаты движения фигуры
    :param size: Размер поля
    :param down: Координата фигуры вниз от 1 точки поля
    :param right: Координата фигуры вправо от 1 точки поля
    :return:
    """
    coords = []
    # Все возможные движения от координаты фигруы фигуры; 1 - вниз/вверх, 2 - влево/вправо
    # Координаты возможного движения начинаются слева сверху направо
    moves = [
        (-2, -1), (-2, 1),
        (-1, -2), (-1, 0), (-1, 2),
        (0, -1), (0, 1),
        (1, -2), (1, 0), (1, 2),
        (2, -1), (2, 1)
    ]
    # Переборка координат возможных движений
    for i in moves:
        # Проверка на нахождение координат на поле
        if 0 <= down + i[0] < size and 0 <= right + i[1] < size:
            coords.append((down + i[0], right + i[1]))
    return coords


def figures(size, n: int, k: int, coords_k: list):
    """
    Функция раставляет уже поставленные фигуры, а также запускает рекурсивную функцию

    :param size: Размер поля
    :param n: Количество фигур
    :param k: Количество уже раставленных фигур
    :param coords_k: Координаты раставленных фигур
    :return:
    """
    coords_of_movemets = []
    list_of_placed_figures = []
    file = open('output.txt', 'w')

    def counting(size, figures: list, coords_of_movement: list, count: int, start_down, start_right) -> int:
        """
        Рекурсивная функция, которая расставляет фигуры с учетом возможных координат
        :param size: Размер поля
        :param figures: Список с раставленными фигурами
        :param coords_of_movement: Список с координатами, куда нельзя поставить фиугуру
        :param count:   Подсчет количества возможных вариантов постановки фигур
        :param start_down: переменная для того, чтобы последующая фигура не ставилось на координатах, меньших,
        чем предыдущая поставленная фигура
        :param start_right: ^
        :return:
        """
        global a
        # Проверка проставлены ли все фигуры
        if len(figures) == n:
            figures += list_of_placed_figures

            # Если это первая комбинация,то запускается функция, которая выводит ее на консоль
            if a == 0:
                print_first_combination(size, figures)
                a = 1

            # Вывод в файл output.txt комбинации расположения фигур
            for i in range(0, n + len(list_of_placed_figures)):
                if i != n + len(list_of_placed_figures) - 1:
                    file.write(f'{figures[i]} ')
                else:
                    file.write(f'{figures[i]}\n')

            return count + 1

        for down in range(start_down, size):
            for right in range(start_right if down == start_down else 0, size):
                if (down, right) not in figures and (down, right) not in coords_of_movement:
                    new_coords_of_movement = movements(size, down, right)
                    count = counting(
                        size,
                        figures + [(down, right)],
                        coords_of_movement + new_coords_of_movement,
                        count,
                        down,
                        right
                    )
        return count

    # Постановка уже раставленных фигур
    for i in range(0, k):
        coords_of_movemets += [(coords_k[i][0], coords_k[i][1])]
        coords_of_movemets += movements(size, coords_k[i][0], coords_k[i][1])
        list_of_placed_figures += [(coords_k[i][0], coords_k[i][1])]

    # Запуск рекурсивной функции
    test = counting(size, [], coords_of_movemets, 0, 0, 0)
    file.close()
    print(f"Количество вариантов расстановки: {test}")


def print_first_combination(size, f_combination) -> None:
    """
    Функция выводит игровое поле с первой комбинацией расположения фигур
    :param size: Размер поля
    :param f_combination: Список с координатами фигур
    :return:
    """
    first_combination_movements = []

    # Получение возможных движений фигур
    for i in f_combination:
        first_combination_movements += movements(size, i[0], i[1])
    pole = []

    # Создание поля
    for i in range(0, size):
        pole.append(['0']*size)
    # Обозначение координат движения
    for i in first_combination_movements:
        pole[i[0]][i[1]] = '*'
    # Обозначение координат фигур
    for i in f_combination:
        pole[i[0]][i[1]] = '#'
    # Вывод поля
    for i in pole:
        i = ' '.join(i)
        print(i)


with open('input.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    first_line = lines[0].split()
    size = int(first_line[0])
    kolvo = int(first_line[1])
    kolvo_placed = int(first_line[2])
    placed_coords = []
    for line in lines[1:]:
        coords = line.split()
        placed_coords.append([int(coords[0]), int(coords[1])])
print(f"Размер доски: {size}, Нужно поставить фигур: {kolvo}, Уже стоят фигур:  {kolvo_placed}")
a = 0
figures(size, kolvo, kolvo_placed, placed_coords)
