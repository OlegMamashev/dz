import sys
from PySide6.QtCore import QSize, Qt, Signal, QThreadPool, Slot, QRunnable, QObject
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QLineEdit,
                               QWidget, QLabel, QPushButton, QGridLayout)


class Figure:
    """
    Шахматная фигура
    """
    def __init__(self, position: tuple, board_size: int):
        """

        :param position: координаты фигуры в кортеже
        :param board_size: размеры поля
        """
        self.position = position
        self.board_size = board_size

    def movements(self) -> set:
        """
        Возвращает все возможные позиции аттак в виде кортежей в множестве
        :return:
        """
        moves = [
            (-2, -1), (-2, 1),
            (-1, -2), (-1, 0), (-1, 2),
            (0, -1), (0, 1),
            (1, -2), (1, 0), (1, 2),
            (2, -1), (2, 1)
        ]

        coords = set()
        for i in moves:
            if 0 <= self.position[0] + i[0] < self.board_size and 0 <= self.position[1] + i[1] < self.board_size:
                coords.add((self.position[0] + i[0], self.position[1] + i[1]))
        return coords


class Board:
    """
    Управляет доской и расстановкой фигур на неё
    """
    def __init__(self, n: int):
        """

        :param n: размер доски
        """
        self.size = n
        self.figures = []
        self.block_coords = set()
        self.placed_figures = []
        self.placed_block_coords = set()

    def add_figure(self, figure: Figure) -> bool:
        """
        Добавляет новую фигуру, если это позволяет позиция
        :param figure: фигура класса Figure
        :return:
        """
        if self.check_attack(figure.position) is None:
            return False
        self.figures.append(figure)
        self.block_coords.add(figure.position)
        # self.block_coords + figure.movements()
        self.block_coords.update(figure.movements())
        return True

    def add_placed_figure(self, figure: Figure) -> bool:
        """
        Добавляет на поле уже стояющую фигуру, если это позволяет позиция
        :param figure: фигура класса Figure
        :return:
        """
        if self.check_attack(figure.position) is None:
            return False
        self.placed_figures.append(figure)
        self.placed_block_coords.add(figure.position)
        self.placed_block_coords.update(figure.movements())
        return True

    def check_attack(self, coord: tuple) -> tuple | None:
        """
        Проверяет, не находится ли позиция под атакой
        :param coord: координаты позиции в кортеже
        :return:
        """
        if coord not in self.get_block_coords():
            return coord
        else:
            return None

    def get_figure_pos(self) -> list:
        """
        Получение расположения всех фигур в списке
        :return:
        """
        return [figure.position for figure in self.figures] + [figure.position for figure in self.placed_figures]

    def get_block_coords(self) -> set:
        """
        Получение всех заблокированных позиций в виде множества
        :return:
        """
        all_block_coords = self.block_coords.union(self.placed_block_coords)
        return all_block_coords

    def remove_figure(self) -> None:
        """
        Убирает последнюю размещенную фигуру с поля
        :return:
        """
        if len(self.figures) != 0:
            del self.figures[-1]
            self.block_coords = set()
            for figure in self.figures:
                self.block_coords.add(figure.position)
                self.block_coords.update(figure.movements())


class Signals(QObject):
    first_combination_signal = Signal(list, set)


class Main(QRunnable):
    """
    Вычисляет все допустимые комбинации расположения фигур
    """

    def __init__(self, place_fig_num: int, board_size: int, placed_fig: list | None, board: Board):
        """

        :param place_fig_num: Количество фигур, которые нужно расставить
        :param board_size: Размер шахматной доски
        :param placed_fig: Список с расставленными фиуграми
        :param board: Шахматная доска класса Board
        """
        super().__init__()

        self.signals = Signals()
        self.file = None
        self.place_fig_num = place_fig_num
        self.board_size = board_size
        self.placed_fig = placed_fig
        self.board = board
        self.combination_number = 0

    def write_output(self, file):
        """
        Записывает комбинацию в файл
        :param file:
        :return:
        """
        figures_list = self.board.get_figure_pos()
        for i in range(0, len(figures_list)):
            if i != len(figures_list) - 1:
                file.write(f'{figures_list[i]} ')
            else:
                file.write(f'{figures_list[i]}\n')

    def run(self):
        """
        Основная функция класса Main
        :return:
        """

        # Добавляем расставленные фигуры если такие имеются
        if self.placed_fig:
            for i in self.placed_fig:
                self.board.add_placed_figure(Figure(i, self.board_size))
        print(self.board)

        def counting(start_y, start_x):
            """
            Рекурсивная функция, которая расставляет фигуры с учетом возможных координат
            :param start_y: переменная для того, чтобы последующая фигура не ставилось на координатах, меньших,
        чем предыдущая поставленная фигура
            :param start_x: ^
            :return:
            """
            if len(self.board.figures) == self.place_fig_num:
                self.combination_number += 1
                # print(self.board.get_figure_pos())

                if self.combination_number == 1:
                    self.signals.first_combination_signal.emit(self.board.get_figure_pos(),
                                                               self.board.get_block_coords())
                    print('412')
                    self.file = open('output.txt', 'w')

                self.write_output(self.file)
                return

            for y in range(start_y, self.board_size):
                for x in range(start_x if y == start_y else 0, self.board_size):
                    if self.board.add_figure(Figure((y, x), self.board_size)):
                        counting(y, x)
                        self.board.remove_figure()
        counting(0, 0)
        if self.file:
            self.file.close()


class BoardGui(QWidget):
    """
    Отображает первую возможную комбинацию расстановки фигур
    Белый квадрат - пустая клетка
    Красный квадрат - фигура
    Синий квадрат - место атаки
    """
    def __init__(self, board_size: int, placed_fig, block_coords):
        """

        :param board_size: Размер шахматной доски
        :param placed_fig: Список с позициями фигур в кортеже
        :param block_coords: Множество с заблокированными позициями в кортеже
        """
        super().__init__()
        self.button_clicked = False
        self.squares = []

        self.setWindowTitle("First combination")
        self.layout = QVBoxLayout(self)

        self.grid_layout_widget = QWidget()
        self.grid_layout = QGridLayout(self.grid_layout_widget)
        self.layout.addWidget(self.grid_layout_widget)

        self.next_button = QPushButton("Записать в файл")
        self.next_button.clicked.connect(self.next_button_clicked)
        self.layout.addWidget(self.next_button)

        self.exit_button = QPushButton("Выйти")
        self.exit_button.clicked.connect(self.exit_button_clicked)
        self.layout.addWidget(self.exit_button)

        for x in range(board_size):
            x_line = []
            for y in range(board_size):
                square = QLabel()
                if board_size > 10:
                    square.setFixedSize(20, 20)
                else:
                    square.setFixedSize(40, 40)
                square.setStyleSheet("background-color: white")
                self.grid_layout.addWidget(square, x, y)
                x_line.append(square)
            self.squares.append(x_line)

        for i in block_coords:
            self.squares[i[0]][i[1]].setStyleSheet("background-color: blue")

        for i in placed_fig:
            self.squares[i[0]][i[1]].setStyleSheet("background-color: red")

    def next_button_clicked(self):
        self.button_clicked = True

    def exit_button_clicked(self):
        self.close()


class InputCoords(QWidget):
    """
    Окно для ввода координат уже стоящих фигур
    """
    def __init__(self, number_of_placed_figures: int, board_size: int):
        """

        :param number_of_placed_figures: Количество уже размещенных фигур
        :param board_size: Размеры шахматной доски
        """
        super().__init__()
        self.n = number_of_placed_figures
        self.board_size = board_size
        self.board = None
        self.coords = []
        self.coords_output = []
        self.layout = QVBoxLayout(self)

        self.input_coords_text = QLabel("Введите координаты:")
        self.layout.addWidget(self.input_coords_text)

        if self.n > 1:
            for coord in range(self.n):
                coord = QLineEdit()
                # coord.textChanged.connect(self.check_coord_inputs)
                self.layout.addWidget(coord)
                self.coords.append(coord)
        else:
            coord = QLineEdit()
            # coord.textChanged.connect(self.check_coord_inputs)
            self.layout.addWidget(coord)
            self.coords.append(coord)

        self.next_text = QLabel("Создать доску?")
        self.layout.addWidget(self.next_text)

        self.ok_button = QPushButton("Да")
        self.ok_button.clicked.connect(self.ok_clicked)
        # self.ok_button.setEnabled(False)
        self.layout.addWidget(self.ok_button)

        self.cancel_button = QPushButton("Нет")
        self.cancel_button.clicked.connect(self.cancel_clicked)
        self.layout.addWidget(self.cancel_button)

    # def check_coord_inputs(self, coord):
    #     if coord != '':
    #         k = coord.split()
    #         if len(k) > 2:
    #             coord = f'{k[0]} {k[1]}'
    #
    #         if len(k) == 2:
    #             if int(k[0]) > self.board_size:
    #                 coord = f'20 {k[1]}'
    #             if int(k[1]) > self.board_size:
    #                 coord = f'{k[0]} 20'
    #             self.ok_button.setEnabled(True)
    #             return coord
    def ok_clicked(self):
        coords = []
        for coord in self.coords:
            coord_text = coord.text().strip().split()
            coords.append((int(coord_text[0]), int(coord_text[1])))
        self.coords_output = coords
        self.board = Board(self.board_size)
        self.close()

    def cancel_clicked(self):
        self.close()


class Gui(QMainWindow):
    """
    Главное окно программы
    """
    def __init__(self):
        super().__init__()

        self.create_b = None
        self.draw_b = None
        self.main = None
        self.board = None
        self.placed_fig_coords = None
        self.thread_pool = QThreadPool()

        self.setWindowTitle("Chess")
        self.setFixedSize(QSize(400, 360))

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.layout = QVBoxLayout(central_widget)

        self.input_size_text = QLabel("Размер доски (N)")
        self.layout.addWidget(self.input_size_text)

        self.input_size = QLineEdit()
        self.input_size.setValidator(QIntValidator(0, 20))
        self.input_size.textChanged.connect(self.check_inputs)
        self.layout.addWidget(self.input_size)

        self.input_place_fig_text = QLabel("Кол-во требуемых фигур (L)")
        self.layout.addWidget(self.input_place_fig_text)

        self.input_place_fig = QLineEdit()
        self.input_place_fig.setValidator(QIntValidator(0, 20*20-1))
        self.input_place_fig.textChanged.connect(self.check_inputs)
        self.layout.addWidget(self.input_place_fig)

        self.input_placed_fig_text = QLabel("Кол-во размещённых фигур (K)")
        self.layout.addWidget(self.input_placed_fig_text)

        self.input_placed_fig = QLineEdit()
        self.input_placed_fig.setValidator(QIntValidator(0, 20*20-1))
        self.layout.addWidget(self.input_placed_fig)

        self.create_board_button = QPushButton("Создать доску")
        self.create_board_button.clicked.connect(self.create_board_clicked)
        self.create_board_button.setEnabled(False)
        self.layout.addWidget(self.create_board_button)

        self.draw_board_button = QPushButton("Нарисовать доску")
        self.draw_board_button.clicked.connect(self.draw_board_clicked)
        self.draw_board_button.setEnabled(False)
        self.layout.addWidget(self.draw_board_button)

        self.exit_button = QPushButton("Выход")
        self.exit_button.clicked.connect(self.exit_clicked)
        self.layout.addWidget(self.exit_button)

    def check_inputs(self):
        """
        Проверяет поля ввода на допустимые значения и разблокирует кнопку создания доски
        :return:
        """
        if self.input_size.text() != '' and self.input_place_fig.text() != '':
            if int(self.input_size.text()) > 20:
                self.input_size.setText('20')
            if int(self.input_place_fig.text()) > 20*20-1:
                self.input_place_fig.setText(f'{20*20-1}')
            self.create_board_button.setEnabled(True)

    def create_board_clicked(self):
        if self.input_placed_fig.text():
            self.create_b = InputCoords(int(self.input_placed_fig.text()), int(self.input_size.text()))
            self.create_b.show()
        else:
            self.board = Board(int(self.input_size.text()))
        self.draw_board_button.setEnabled(True)

    def draw_board_clicked(self):
        """
        Кнопка запускает класс Main
        :return:
        """
        if self.create_b:
            self.placed_fig_coords = self.create_b.coords_output
            self.board = self.create_b.board
        self.main = Main(int(self.input_place_fig.text()), int(self.input_size.text()),
                         self.placed_fig_coords, self.board)

        self.main.signals.first_combination_signal.connect(self.show_first_combination)
        self.thread_pool.start(self.main)

    @Slot(list, set)
    def show_first_combination(self, figures, block_coords):
        """
        Запускается при получении первой комбинации в Main и запускает BoardGui для её отображения
        :param figures: Список с позициями фигур в кортеже
        :param block_coords: Множество с заблокированными позициями в кортеже
        :return:
        """
        self.draw_b = BoardGui(int(self.input_size.text()), figures, block_coords)
        self.draw_b.show()
        # print(self.draw_b.button_clicked)
        # while not self.draw_b.button_clicked:
        #     QApplication.processEvents()

    def exit_clicked(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = Gui()
    gui.show()
    app.exec()
