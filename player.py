from colorama import Fore, Back, Style
import random
import board


class Player:
    def __init__(self, name):
        self.name = name
        self.board = board.Board()
        self.ships = [4, 3, 2, 1]

    def get_board(self):
        return self.board.matrix

    def star_put_ships(self):
        print(
            "ES HORA DE COLOCAR TUS BARCOS EN EL TABLERO.\n"
            "*NOTA* Para colocar el barco necesitas:\n"
            "   1- Coordenada fila y columna (x,y)\n"
            "   2- Posiciones de eslora (1...4)\n"
            "   3- Orientación Horizontal o Vertical (h,v)\n")
        while sum(self.ships) > 0:
            print("TIENES DISPONIBLE: \n"
                  f"   * {self.ships[0]} barcos de 1 posición de eslora\n"
                  f"   * {self.ships[1]} barcos de 2 posiciones de eslora\n"
                  f"   * {self.ships[2]} barcos de 3 posiciones de eslora\n"
                  f"   * {self.ships[3]} barcos de 4 posiciones de eslora"
                  "\n")
            while True:
                coordinate = input("Entre la cordenada Ej '1,2': ")
                if len(coordinate) == 3:
                    aux = coordinate.split(",")
                    if len(aux) == 2 and aux[0].isnumeric() and aux[1].isnumeric() and 0 <= int(
                            aux[0]) <= 9 and 0 <= int(aux[1]) <= 9:
                        row = int(aux[0]) + 1
                        col = int(aux[1]) + 1
                        break
                print(Fore.RED + "COORDENADAS INCORRECTAS." + Style.RESET_ALL)

            while True:
                str_length = []
                if self.ships[0] != 0:
                    str_length.append(1)
                if self.ships[1] != 0:
                    str_length.append(2)
                if self.ships[2] != 0:
                    str_length.append(3)
                if self.ships[3] != 0:
                    str_length.append(4)

                length = input(f"INTRODUCE LA TAMAÑO DE ESLORA, OPCIONES:  {str(str_length)}: ")
                if length.isnumeric() and length in str(str_length):
                    break
                print(Fore.RED + "ESLORA INCORRECTA." + Style.RESET_ALL)

            while True:
                orientation = input("Entre la orientacion Ej: V o H: ")
                if len(orientation) == 1 and orientation.lower() in "vh":
                    break
                print(Fore.RED + "ESLORA INCORRECTA." + Style.RESET_ALL)

            if self.board.is_place_boat(row, col, length, orientation):
                self.board.put_boat(row, col, length, orientation)
                self.ships[int(length) - 1] -= 1
                print("\n")
                print(Fore.YELLOW + f"TABLERO USUARIO: {self.name}" + Style.RESET_ALL)
                print(self.get_board())
            else:
                print(Fore.RED + "EL BARCO NO SE PUEDE COLOCAR EN ESA POSICION." + Style.RESET_ALL)

    def place_all_ships_randomly(self):
        count = 3
        while sum(self.ships) > 0:

            #   COORDENADAS ALEATORIAS
            row = random.randint(1, 10)
            col = random.randint(1, 10)

            #   DISPONIBILIDAD DE ESLORA DESDE 1 a 4
            while True:
                if self.ships[count] > 0:
                    break
                else:
                    count = count - 1

            length = count + 1

            # Genera un número aleatorio entre 0 y 1
            random_number = random.random()
            if random_number < 0.5:
                orientation = "h"
            else:
                orientation = "v"

            if self.board.is_place_boat(row, col, length, orientation):
                self.board.put_boat(row, col, length, orientation)
                self.ships[int(length) - 1] -= 1
        print(self.get_board())

    def shoot(self, turno):
        if turno:
            while True:
                coordinate = input("Entre la cordenada de disparo Ej '1,2': ")
                if len(coordinate) == 3:
                    aux = coordinate.split(",")
                    if len(aux) == 2 and aux[0].isnumeric() and aux[1].isnumeric() and 0 <= int(
                            aux[0]) <= 9 and 0 <= int(aux[1]) <= 9:
                        row = int(aux[0]) + 1
                        col = int(aux[1]) + 1
                        break
                print(Fore.RED + "COORDENADAS INCORRECTAS." + Style.RESET_ALL)
        else:
            row = random.randint(1, 10)
            col = random.randint(1, 10)

        if self.board.matrix[row, col] == "O":
            if self.board.is_alone(row, col):
                self.board.matrix[row, col] = "💥"
            else:
                self.board.matrix[row, col] = "💣"
                self.board.find_first()
            return True
        elif self.board.matrix[row, col] == " ":
            self.board.matrix[row, col] = "🌊"
            return False
        elif self.board.matrix[row, col] == "🌊":
            return False
