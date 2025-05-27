import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLineEdit, QWidget, QLabel, QPushButton


class Figure:
    def __init__(self, position: tuple):
        self.position = position

    def movements(self, board_size: int):
        moves = [
            (-2, -1), (-2, 1),
            (-1, -2), (-1, 0), (-1, 2),
            (0, -1), (0, 1),
            (1, -2), (1, 0), (1, 2),
            (2, -1), (2, 1)
        ]

        coords = []
        for i in moves:
            if 0 <= self.position[0] + i[0] < board_size and 0 <= self.position[1] + i[1] < board_size:
                coords.append((position[0] + i[0], position[1] + i[1]))
        return coords


class Board:
    def __init__(self, n: int):
        self.size = n
        self.figures = []
        self.block_coords = set()

    def add_figure(self, figure: Figure) -> bool:
        if self.check_attack(figure.position) is None:
            return False
        self.figures.append(figure)
        self.block_coords.add(figure.position)
        self.block_coords + figure.movements(self.size)
        return True

    def check_attack(self, coord: tuple) -> tuple | None:
        if coord not in self.block_coords:
            return coord
        else:
            return None

    def get_figure_pos(self):
        return [figure.position for figure in self.figures]


class Main:
    def __init__(self, place_fig_num):
        self.place_fig_num = place_fig_num
        self.combination_number = 0

    def place_fig(self):
        pass




class BoardGui:
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First combination")
        self.setFixedSize(QSize(500, 500))
        self.layout = QVBoxLayout(self)


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
            coords.append((coord_text[0], coord_text[1]))
        self.coords_output = coords
        self.close()


class Gui(QMainWindow):
    def __init__(self):
        super().__init__()

        self.create_b = None
        self.draw_b = None
        self.placed_fig_coords = None

        self.setWindowTitle("Chess")
        self.setFixedSize(QSize(400, 300))

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
        if self.create_b.coords_output:
            self.placed_fig_coords = self.create_b.coords_output

        self.draw_b = BoardGui()
        self.draw_b.show()

    def exit_clicked(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = Gui()
    gui.show()
    app.exec()
