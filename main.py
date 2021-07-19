import time


class QueenPlaces:
    def __init__(self, size):
        self.size = size
        self.number_of_solutions = 0

    def solve(self):
        """
        Solve the eight queen problem
        """
        rows = [""] * self.size
        self.find_queens(rows, 0)

    def find_queens(self, rows, column_index):
        """
        Find all possible placements and check with check_position
        """
        if column_index == self.size:
            self.show(rows)
            self.number_of_solutions += 1
            return True

        for column in range(self.size):
            if self.check_position(rows, column_index, column):
                rows[column_index] = column
                self.find_queens(rows, column_index + 1)

    def check_position(self, rows, column_index, column) -> bool:
        """
        Check for any intersections in the horizontal, vertical and diagonal axis.

        :return: bool
            True if there is no intersection
            False if there is intersection
        """

        for i in range(column_index):
            if rows[i] == column or rows[i] - i == column - column_index or rows[i] + i == column + column_index:
                return False
        return True

    def show(self, rows: list, just_terminal: bool = False):
        """
        Shows the results found

        :param rows: list
            List of column indexes for correctly found positions.
            (e.g. [0, 4, 7, 5, 2, 6, 1, 3])

        :param just_terminal:
            If True it only shows in terminal.
            If False, it shows on the image with cv2.
        """

        rows2d = [["Q" if column == rows[row] else "" for column in range(self.size)] for row in range(self.size)]

        if just_terminal:
            for row in rows2d:
                print(row)
        else:
            # TODO: Show in board with opencv
            pass


if __name__ == '__main__':
    size = 8

    qp = QueenPlaces(size)
    start_time = time.time()
    qp.solve()
    end_time = time.time()
    print(f"Founded {qp.number_of_solutions} solution in {str(end_time - start_time)[:7]} seconds.")
