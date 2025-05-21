class Board:
    def __init__(self, n: int):
        self.size = n
        self.figures = []
        self.block_coords = set()

    def add_figure(self, figure: Figure) -> Bool:
        if self.check_attack(figure.position) is None:
            return False
        self.figures.append(figure)
        self.block_coords.add(figure.position)
        self.block_coords + figure.movements(self.size)
        return True

    def check_attack(self, coord: tuple) -> tuple/None:
        if coord not in self.block_coords:
            return coord
        else:
            return None

    def get_figure_pos(self):
        return [figure.position for figure in self.figures]


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
            if 0 <= position[0] + i[0] < board_size and 0 <= position[1] + i[1] < board_size:
                coords.append((position[0] + i[0], position[1] + i[1]))
        return coords


class Gui:
    pass
