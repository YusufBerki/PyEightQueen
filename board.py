import cv2


class Board():
    def __init__(self, size):
        self.size = size
        self.create()

    def create(self):
        """
        Create n x n chessboards based on size value.
        """
        pass

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

    def draw(self):
        """
        Draw & show pieces and board on image
        """
