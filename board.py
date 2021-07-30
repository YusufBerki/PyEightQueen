import os
import cv2
import string
import numpy as np
from utils import PIECES, COLOR_SCHEME


def overlay_transparent(background, overlay, x, y):
    background_width = background.shape[1]
    background_height = background.shape[0]

    overlay_image = overlay[..., :4]
    mask = overlay[..., 3:] / 255.0
    background[y:y + h, x:x + w] = (1.0 - mask) * background[y:y + h, x:x + w] + mask * overlay_image
    return background


class Board():
    def __init__(self, size, mode=1, cell_length=100):
        self.size = size
        self.cell_length = cell_length
        self.mode = mode
        self.create()

    def create(self):
        """
        Create n x n chessboards based on size value.
        """
        get_row = lambda size, shift: [{"type": (cell_index + shift) % 2, "piece": None} for cell_index in range(size)]
        self.board = [get_row(self.size, _ % 2) for _ in range(self.size)]

        self.panel_length = self.cell_length * self.size
        self.panel = np.zeros([self.panel_length, self.panel_length, 3], dtype=np.uint8)
        self.panel.fill(255)
        for row_index, row in enumerate(self.board):
            for column_index, column in enumerate(row):
                cell_start = (row_index * self.cell_length, column_index * self.cell_length)
                cell_end = ((row_index + 1) * self.cell_length, (column_index + 1) * self.cell_length)

                self.panel = cv2.rectangle(self.panel, cell_start, cell_end, COLOR_SCHEME[self.mode][column['type']], -1)

        self.panel = cv2.cvtColor(self.panel, cv2.COLOR_BGR2BGRA)

    def put(self, piece: str, cell: tuple) -> bool:
        """
        Put the desired piece in the desired cell on the chessboard.

        :param piece: str
            Name of piece
        :param cell: tuple, (int,int)
            Coordinates of the area on the 2D chessboard where you want to place the piece.
            It must be in the form of a 2-element tuple. On an 8x8 board it should be;
                (0,0) for the top left cell (A8)
                or
                (7,7) for the bottom right cell (H1).

        :return: bool
            Status of the put operation as boolean
        """

        row, column = cell
        self.board[row][column]['piece'] = piece
        return True

    def draw(self):
        """
        Draw & show pieces and board on image
        """

        for row_index, row in enumerate(self.board):
            for column_index, column in enumerate(row):
                if not column['piece']:
                    continue

                xmin = row_index * self.cell_length
                ymin = column_index * self.cell_length
                xmax = (row_index + 1) * self.cell_length
                ymax = (column_index + 1) * self.cell_length

                piece_img = self._get_piece(column['piece'])
                mask = piece_img[..., 3:] / 255.0
                self.panel[ymin:ymax, xmin:xmax] = (1.0 - mask) * self.panel[ymin:ymax, xmin:xmax] + mask * piece_img

    def show(self):
        cv2.imshow("Solution", self.panel)
        cv2.waitKey()

    def write(self, path):
        cv2.imwrite(path, self.panel)

    def _get_piece(self, piece_name):
        piece = PIECES.get(piece_name, None)
        if not piece:
            raise KeyError(f"Wrong piece name. Use: {PIECES.keys()}")

        piece_img = piece.get('img', None)

        if piece_img is None:
            piece_path = piece['path']

            piece_img = cv2.imread(piece_path, cv2.IMREAD_UNCHANGED)
            piece_img = cv2.resize(piece_img, (self.cell_length, self.cell_length))

            PIECES[piece_name]['img'] = piece_img

        return piece_img


if __name__ == '__main__':
    board = Board(size=8)
    board.draw()
