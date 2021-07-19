class QueenPlaces:
    def __init__(self, size):
        self.size = size

    def solve(self):
        """
        Solve the eight queen problem
        """

    def find_queens(self):
        """
        Find all possible placements and check with check_position
        """

    def check_position(self) -> bool:
        """
        Check for any intersections in the horizontal, vertical and diagonal axis.

        :return: bool
            True if there is no intersection
            False if there is intersection
        """

    def show(self, just_terminal: bool = False):
        """
        Shows the results found
        :param just_terminal:
            If True it only shows in terminal.
            If False, it shows on the image with cv2.
        """


if __name__ == '__main__':
    size = 8

    qp = QueenPlaces(size)
    qp.solve()
