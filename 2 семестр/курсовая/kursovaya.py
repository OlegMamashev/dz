import sys
from PySide6.QtCore import QSize, Qt, Signal, QThreadPool, Slot, QRunnable, QObject
from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QLineEdit,
                               QWidget, QLabel, QPushButton, QGridLayout)


class Figure:
    def __init__(self, position: tuple, board_size: int):
        self.position = position
        self.board_size = board_size

    def movements(self):
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
    def __init__(self, n: int):
        self.size = n
        self.figures = []
        self.block_coords = set()
        self.placed_figures = []
        self.placed_block_coords = set()

    def add_figure(self, figure: Figure) -> bool:
        if self.check_attack(figure.position) is None:
            return False
        self.figures.append(figure)
        self.block_coords.add(figure.position)
        # self.block_coords + figure.movements()
        self.block_coords.update(figure.movements())
        return True

    def add_placed_figure(self, figure: Figure) -> bool:
        if self.check_attack(figure.position) is None:
            return False
        self.placed_figures.append(figure)
        self.placed_block_coords.add(figure.position)
        self.placed_block_coords.update(figure.movements())
        return True

    def check_attack(self, coord: tuple) -> tuple | None:
        # if coord not in self.block_coords and coord not in self.placed_block_coords:
        if coord not in self.get_block_coords():
            return coord
        else:
            return None

    def get_figure_pos(self) -> list:
        return [figure.position for figure in self.figures] + [figure.position for figure in self.placed_figures]

    def get_block_coords(self):
        all_block_coords = self.block_coords.union(self.placed_block_coords)
        return all_block_coords

    def remove_figure(self) -> None:
        # self.figures = []
        # self.block_coords = set()
        if len(self.figures) != 0:
            del self.figures[-1]
            self.block_coords = set()
            for figure in self.figures:
                self.block_coords.add(figure.position)
                self.block_coords.update(figure.movements())


class Signals(QObject):
    first_combination_signal = Signal(list, set)


class Main(QRunnable):

    def __init__(self, place_fig_num: int, board_size: int, placed_fig: list | None):
        super().__init__()

        self.signals = Signals()
        self.file = None
        self.place_fig_num = place_fig_num
        self.board_size = board_size
        self.placed_fig = placed_fig
        self.board = Board(board_size)
        self.combination_number = 0

    def write_output(self, file):
        figures_list = self.board.get_figure_pos()
        for i in range(0, len(figures_list)):
            if i != len(figures_list) - 1:
                file.write(f'{figures_list[i]} ')
            else:
                file.write(f'{figures_list[i]}\n')

    def run(self):

        # Добавляем расставленные фигуры
        if self.placed_fig:
            for i in self.placed_fig:
                self.board.add_placed_figure(Figure(i, self.board_size))

        self.file = open('output.txt', 'w')

        def counting(start_y, start_x):
            if len(self.board.figures) == self.place_fig_num:
                self.combination_number += 1
                # print(self.board.get_figure_pos())

                if self.combination_number == 1:
                    self.signals.first_combination_signal.emit(self.board.get_figure_pos(),
                                                               self.board.get_block_coords())

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
    def __init__(self, board_size, placed_fig, block_coords):
        super().__init__()
        # self.board_size = board_size
        # self.placed_fig = placed_fig
        # self.block_coords = block_coords
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
        self.layout.addWidget(self.exit_button)

        for x in range(board_size):
            x_line = []
            for y in range(board_size):
                square = QLabel()
                square.setFixedSize(20, 20)
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


class InputCoords(QWidget):
    def __init__(self, number_of_placed_figures: int):
        super().__init__()
        self.n = number_of_placed_figures
        self.coords = []
        self.coords_output = []
        self.layout = QVBoxLayout(self)

        self.input_coords_text = QLabel("Введите координаты:")
        self.layout.addWidget(self.input_coords_text)

        if self.n > 1:
            for coord in range(self.n):
                coord = QLineEdit()
                self.layout.addWidget(coord)
                self.coords.append(coord)
        else:
            coord = QLineEdit()
            self.layout.addWidget(coord)
            self.coords.append(coord)

        self.next_text = QLabel("Создать доску?")
        self.layout.addWidget(self.next_text)

        self.ok_button = QPushButton("Да")
        self.ok_button.clicked.connect(self.ok_clicked)
        self.layout.addWidget(self.ok_button)

        self.cancel_button = QPushButton("Нет")
        self.layout.addWidget(self.cancel_button)

    def ok_clicked(self):
        coords = []
        for coord in self.coords:
            coord_text = coord.text().strip().split()
            coords.append((int(coord_text[0]), int(coord_text[1])))
        self.coords_output = coords
        self.close()


class Gui(QMainWindow):
    def __init__(self):
        super().__init__()

        self.create_b = None
        self.draw_b = None
        self.main = None
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
        self.layout.addWidget(self.input_size)

        self.input_place_fig_text = QLabel("Кол-во требуемых фигур (L)")
        self.layout.addWidget(self.input_place_fig_text)

        self.input_place_fig = QLineEdit()
        self.layout.addWidget(self.input_place_fig)

        self.input_placed_fig_text = QLabel("Кол-во размещённых фигур (K)")
        self.layout.addWidget(self.input_placed_fig_text)

        self.input_placed_fig = QLineEdit()
        self.layout.addWidget(self.input_placed_fig)

        self.create_board_button = QPushButton("Создать доску")
        self.create_board_button.clicked.connect(self.create_board_clicked)
        self.layout.addWidget(self.create_board_button)

        self.draw_board_button = QPushButton("Нарисовать доску")
        self.draw_board_button.clicked.connect(self.draw_board_clicked)
        self.layout.addWidget(self.draw_board_button)

        self.exit_button = QPushButton("Выход")
        self.exit_button.clicked.connect(self.exit_clicked)
        self.layout.addWidget(self.exit_button)

    def create_board_clicked(self):
        self.create_b = InputCoords(int(self.input_placed_fig.text()))
        self.create_b.show()

    def draw_board_clicked(self):
        if self.create_b:
            self.placed_fig_coords = self.create_b.coords_output

        self.main = Main(int(self.input_place_fig.text()), int(self.input_size.text()), self.placed_fig_coords)
        self.main.signals.first_combination_signal.connect(self.show_first_combination)
        self.thread_pool.start(self.main)

    @Slot(list, set)
    def show_first_combination(self, figures, block_coords):
        self.draw_b = BoardGui(int(self.input_size.text()), figures, block_coords)
        self.draw_b.show()

    def exit_clicked(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = Gui()
    gui.show()
    app.exec()
