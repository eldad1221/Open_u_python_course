from random import shuffle


class Soduko:

    SQUARE_SIZE = 3

    def __init__(self):
        pass



class Square3x3:

    SQUARE_SIZE = 3
    CELLS = SQUARE_SIZE ** 2
    NUMBERS = [n for n in range(1, CELLS + 1)]

    def __init__(self, mat: list[list[int]] = None) -> None:
        if mat is None:
            numbers = self.NUMBERS.copy()
            shuffle(numbers)
            self._mat = [[numbers[i * self.SQUARE_SIZE+j] for i in range(self.SQUARE_SIZE)] for j in range(self.SQUARE_SIZE)]
        else:
            self._mat = mat

    def get_cell(self, row: int, col: int) -> int:
        return self._mat[row][col]

    def set_cell(self, row: int, col: int, value: int) -> None:
        if 9 < value < 1:
            raise ValueError("Value must be between 1 and 9")
        self._mat[row][col] = value

    def __str__(self) -> str:
        s = ""
        for i in range(self.SQUARE_SIZE):
            for j in range(self.SQUARE_SIZE):
                s = f"{s}{self._mat[i][j]}\t"
            s = f"{s}\n"
        return s

    def all_there(self) -> bool:
        flattened_list = [element for sublist in self._mat for element in sublist]
        is_there = [n in flattened_list for n in range(1, self.CELLS + 1)]
        return not False in is_there

    def whos_there_row(self, row: int, values: list[bool]):
        for i in range(self.SQUARE_SIZE):
            values[self._mat[row][i]] = True

    def whos_there_col(self, col: int, values: list[bool]):
        for i in range(self.SQUARE_SIZE):
            values[self._mat[i][col]] = True


if __name__ == '__main__':
    square3x3 = Square3x3()
    print(square3x3)
    print(square3x3.all_there())


