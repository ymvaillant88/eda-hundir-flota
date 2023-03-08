from colorama import Fore, Back, Style
import player


class Game:

    def __init__(self):
        self.player1 = None
        self.player2 = None
        self.turno = True

    def start_game(self):
        name = input("Entre su nombre: ")
        self.player1 = player.Player(name)
        self.player2 = player.Player("CPU")

        # PASO 1 PEDIR SI DESEA COLOCAR ALEATORIAMENTE LOS BARCOS
        while True:
            put_random = input('Deseas colocar tus barcos aleatoriamente (Y,N)')
            if len(put_random) != 1:
                continue
            elif not put_random.lower() in "yn":
                continue
            else:
                break

        # PASO 2 COLOCAR ALEATORIAMENTE LOS BARCOS
        if put_random.lower() == "y":
            print("\n")
            print(Fore.YELLOW + f"TABLERO USUARIO: {self.player1.name}" + Style.RESET_ALL)
            self.player1.place_all_ships_randomly()
        else:
            # PASO 2 COLOCAR BARCOS MANUALMENTE
            print("\n")
            self.player1.star_put_ships()

        # PASO 3 COLOCAR ALEATORIAMENTE LOS BARCOS DE LA MAQUINA
        print("\n")
        print(Fore.YELLOW + f"TABLERO USUARIO: {self.player2.name}" + Style.RESET_ALL)
        self.player2.place_all_ships_randomly()

        # PASO 4 DISPARO POR TURNO
        while (self.turno and self.player1.board.is_has_boats()) or (
                not self.turno and self.player2.board.is_has_boats()):
            if self.turno:
                print("\n")
                print(Fore.YELLOW + f"**HORA DE DISPARAR**:" + Style.RESET_ALL)
                print(Fore.YELLOW + f"TURNO DE: {self.player1.name}" + Style.RESET_ALL)
                aux = self.player2.shoot(self.turno)
                if not self.player2.board.is_has_boats():
                    print(Fore.YELLOW + f"EL JUGADOR ***{self.player1.name}*** HA HUNDIDO LA FLOTA*:" + Style.RESET_ALL)
                    break
                elif not aux:
                    self.turno = False
                else:
                    self.turno = True
                print(self.player2.get_board())
            else:
                print("\n")
                print(Fore.YELLOW + f"**HORA DE DISPARAR**:" + Style.RESET_ALL)
                print(Fore.YELLOW + f"TURNO DE: {self.player2.name}" + Style.RESET_ALL)
                aux = self.player1.shoot(self.turno)
                if not self.player1.board.is_has_boats():
                    print(Fore.YELLOW + f"EL JUGADOR ***{self.player2.name}*** HA HUNDIDO LA FLOTA*:" + Style.RESET_ALL)
                    break
                elif not aux:
                    self.turno = True
                else:
                    self.turno = False
                print(self.player1.get_board())
