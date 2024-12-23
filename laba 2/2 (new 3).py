class Pole:

    def __init__(self, size):
        # self.x = size
        # self.y
        self.size = size
        self.file = open('output.txt', 'w')

    def movements(self, down, right):
        """
        Функция принимает координаты вниз - влево и возвращает координаты движения фигуры
        :param down: Координата фигуры вниз от 1 точки поля
        :param right: Координата фигуры вправо от 1 точки поля
        :return:
        """
        coords = []
        # Все возможные движения от координаты фигруы фигуры; 1 - вниз/вверх, 2 - влево/вправо
        # Координаты возможного движения начинаются слева сверху направо
        moves = [
            [-2, -1], [-2, 1],
            [-1, -2], [-1, 0], [-1, 2],
            [0, -1], [0, 1],
            [1, -2], [1, 0], [1, 2],
            [2, -1], [2, 1]
        ]
        # Переборка координат возможных движений
        for i in moves:
            # Проверка на нахождение координат на поле
            if (down + i[0]) >= 0 and (right + i[1]) >= 0:
                coords.append([down+i[0], right + i[1]])
        return coords



    # Тут будут фигурки, которые будут ставятся

    def figures(self, n: int, k: int, coords_k: list):
        """
        Функция раставляет уже поставленные фигуры, а также запускает рекурсивную функцию

        :param n: Количество фигур
        :param k: Количество уже раставленных фигур
        :param coords_k: Координаты раставленных фигур
        :return:
        """
        coords_of_movemets = []
        figures = []

        def counting(figures: list, coords_of_movement:list, count: int, start_down, start_right):
            """
            Рекурсивная функция, которая расставляет фигуры с учетом возможных координат
            :param figures: Список с раставленными фигурами
            :param coords_of_movement: Список с координатами, куда нельзя поставить фиугуру
            :param count:   Подсчет количества возможных вариантов постановки фигур
            :param start_down: переменная для того, чтобы последующая фигура не ставилось на координатах, меньших, чем предыдущая поставленная фигура
            :param start_right: ^
            :return:
            """

            # Проверка проставлены ли все фигуры
            if len(figures) == n:
                self.file.write(f'{figures}\n')
                return count + 1

            for down in range(start_down, self.size):
                for right in range(start_right if down == start_down else 0, self.size):
                    if [down, right] not in figures and [down, right] not in coords_of_movement:
                        new_coords_of_movement = self.movements(down, right)
                        count = counting(
                            figures + [[down, right]],
                            coords_of_movement + new_coords_of_movement,
                            count,
                            down,
                            right
                        )
            return count

        # Постановка уже раставленных фигур
        for i in range(0, k):
            coords_of_movemets += [[coords_k[i][0], coords_k[i][1]]]
            coords_of_movemets += self.movements(coords_k[i][0], coords_k[i][1])

        # Запуск рекурсивной функции
        test = counting([], coords_of_movemets, 0, 0, 0)
        print(test)


if __name__ == "__main__":
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
    chess = Pole(size)
    chess.figures(kolvo, kolvo_placed, placed_coords)
