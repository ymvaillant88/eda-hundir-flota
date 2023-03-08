import numpy as np


def init_matrix():
    aux = np.full((11, 11), " ")
    for num in range(11):
        if num == 0:
            aux[0, 0] = "#"
        else:
            aux[num, 0] = str(num - 1)
            aux[0, num] = str(num - 1)
    return aux


class Board:
    def __init__(self):
        self.matrix = init_matrix()

    def is_not_empty(self, row, col):
        if 1 <= row <= 10 and 1 <= col <= 10:
            if self.matrix[row, col] == "O" or self.matrix[row, col] == "💥" or self.matrix[row, col] == "💣":
                return False
            return True
        return False

    def is_available(self, row, col):

        if not self.is_not_empty(row, col):
            return False

        elif 1 <= (row + 1) <= 10 and not self.is_not_empty((row + 1), col):
            return False

        elif 1 <= (row - 1) <= 10 and not self.is_not_empty((row - 1), col):
            return False

        elif 1 <= (col + 1) <= 10 and not self.is_not_empty(row, col + 1):
            return False

        elif 1 <= (col - 1) <= 10 and not self.is_not_empty(row, col - 1):
            return False

        elif 1 <= (row + 1) <= 10 and 1 <= (col + 1) <= 10 and not self.is_not_empty(row + 1, col + 1):
            return False

        elif 1 <= (row - 1) <= 10 and 1 <= (col - 1) <= 10 and not self.is_not_empty(row - 1, col - 1):
            return False

        elif 1 <= (row + 1) <= 10 and 1 <= (col - 1) <= 10 and not self.is_not_empty(row + 1, col - 1):
            return False

        elif 1 <= (row - 1) <= 10 and 1 <= (col + 1) <= 10 and not self.is_not_empty(row - 1, col + 1):
            return False

        else:
            return True

    def is_place_boat(self, row, col, length, orientation):
        for elem in range(int(length)):
            if orientation == "v":
                if not self.is_available(row + elem, col):
                    return False
            elif orientation == "h":
                if not self.is_available(row, col + elem):
                    return False
        return True

    def put_boat(self, row, col, length, orientation):
        for elem in range(int(length)):
            if orientation == "v":
                self.matrix[row + elem, col] = "O"
            elif orientation == "h":
                self.matrix[row, col + elem] = "O"

    def is_has_boats(self):
        for row in range(11):
            for col in range(11):
                if self.matrix[row, col] == "O":
                    return True
        return False

    def is_alone(self, row, col):

        if 1 <= (row + 1) <= 10 and not self.is_not_empty((row + 1), col):
            return False

        elif 1 <= (row - 1) <= 10 and not self.is_not_empty((row - 1), col):
            return False

        elif 1 <= (col + 1) <= 10 and not self.is_not_empty(row, col + 1):
            return False

        elif 1 <= (col - 1) <= 10 and not self.is_not_empty(row, col - 1):
            return False

        elif 1 <= (row + 1) <= 10 and 1 <= (col + 1) <= 10 and not self.is_not_empty(row + 1, col + 1):
            return False

        elif 1 <= (row - 1) <= 10 and 1 <= (col - 1) <= 10 and not self.is_not_empty(row - 1, col - 1):
            return False

        elif 1 <= (row + 1) <= 10 and 1 <= (col - 1) <= 10 and not self.is_not_empty(row + 1, col - 1):
            return False

        elif 1 <= (row - 1) <= 10 and 1 <= (col + 1) <= 10 and not self.is_not_empty(row - 1, col + 1):
            return False

        else:
            return True

    def validate_blow_up_ship(self, row, col, visited=[]):
        visited.append(f"{row}-{col}")
        if 1 <= (row + 1) <= 10 and f"{row + 1}-{col}" not in visited and self.matrix[row + 1, col] == "💣":
            return self.validate_blow_up_ship(row + 1, col, visited)

        elif 1 <= (row - 1) <= 10 and f"{row - 1}-{col}" not in visited and self.matrix[row - 1, col] == "💣":
            return self.validate_blow_up_ship(row - 1, col, visited)

        elif 1 <= (col + 1) <= 10 and f"{row}-{col + 1}" not in visited and self.matrix[row, col + 1] == "💣":
            return self.validate_blow_up_ship(row, col + 1, visited)

        elif 1 <= (col - 1) <= 10 and f"{row}-{col - 1}" not in visited and self.matrix[row, col - 1] == "💣":
            return self.validate_blow_up_ship(row, col - 1, visited)

        else:
            if 1 <= (row + 1) <= 10 and f"{row + 1}-{col}" not in visited and self.matrix[row + 1, col] == "O":
                return False

            elif 1 <= (row - 1) <= 10 and f"{row - 1}-{col}" not in visited and self.matrix[row - 1, col] == "O":
                return False

            elif 1 <= (col + 1) <= 10 and f"{row}-{col + 1}" not in visited and self.matrix[row, col + 1] == "O":
                return False

            elif 1 <= (col - 1) <= 10 and f"{row}-{col - 1}" not in visited and self.matrix[row, col - 1] == "O":
                return False
            else:
                return True

    def blow_up_ship(self, row, col, visited=[]):
        self.matrix[row, col] = "💥"
        if 1 <= (row + 1) <= 10 and f"{row}-{col}" not in visited and self.matrix[row + 1, col] == "💣":
            visited.append(f"{row}-{col}")
            return self.blow_up_ship(row + 1, col, visited)

        elif 1 <= (row - 1) <= 10 and f"{row}-{col}" not in visited and self.matrix[row - 1, col] == "💣":
            visited.append(f"{row}-{col}")
            return self.blow_up_ship(row - 1, col, visited)

        elif 1 <= (col + 1) <= 10 and f"{row}-{col}" not in visited and self.matrix[row, col + 1] == "💣":
            visited.append(f"{row}-{col}")
            return self.blow_up_ship(row, col + 1, visited)

        elif 1 <= (col - 1) <= 10 and f"{row}-{col}" not in visited and self.matrix[row, col - 1] == "💣":
            visited.append(f"{row}-{col}")
            return self.blow_up_ship(row, col - 1, visited)

    def find_first(self):
        for row in range(1, 11):
            for col in range(1, 11):
                if self.matrix[row, col] == "💣":
                    if self.validate_blow_up_ship(row, col):
                        self.blow_up_ship(row, col)
