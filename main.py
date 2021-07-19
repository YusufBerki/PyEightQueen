import time
import cv2
from board import Board


class QueenPlaces:
    def __init__(self, size):
        self.size = size

        self.solutions = []

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
            self.solutions.append(rows.copy())
            self.show(rows)
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

    def show(self, rows: list):
        """
        Shows the results found

        :param rows: list
            List of column indexes for correctly found positions.
            (e.g. [0, 4, 7, 5, 2, 6, 1, 3])
        """

        rows2d = [["Q" if column == rows[row] else "" for column in range(self.size)] for row in range(self.size)]
        print(f"Solution {len(self.solutions)}:")
        for row in rows2d:
            print(row)
        print("\n", "-" * 50, "\n")


if __name__ == '__main__':
    size = 8

    qp = QueenPlaces(size)

    start_time = time.time()

    qp.solve()

    end_time = time.time()

    print(f"Founded {len(qp.solutions)} solution in {str(end_time - start_time)[:7]} seconds.")

    # Show with CV2
    for solution_index, rows in enumerate(qp.solutions):
        board = Board(size=size)
        for row_index, column_index in enumerate(rows):
            board.put('queen', (row_index, column_index))
        board.panel = cv2.putText(board.panel, f'Solution {solution_index}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
        board.draw()
