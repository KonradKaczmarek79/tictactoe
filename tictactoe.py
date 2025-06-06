from collections import Counter
import string


class GameInterface:
    def __init__(self, a1, a2, a3, b1, b2, b3, c1, c2, c3):
        # self.grid = [[a1, a2, a3], [b1, b2, b3], [c1, c2, c3]]
        self.grid = {"1 1": a1, "1 2": a2, "1 3": a3,
                     "2 1": b1, "2 2": b2, "2 3": b3,
                     "3 1": c1, "3 2": c2, "3 3": c3}

    def return_as_list(self):
        # return [self.a1, self.a2, self.a3, self.b1, self.b2, self.b3, self.c1, self.c2, self.c3]
        # return [element for sublist in self.grid for element in sublist ]
        return list(self.grid.values())

    @staticmethod
    def check_count(temp_list):
        counts = Counter(temp_list)
        if abs(counts["X"] - counts["O"]) > 1:
            return False
        return True

    @staticmethod
    def is_the_same_value(symbol, element_1, element_2, element_3):
        """ check if symbol is equal to element_1 and element_2 and element_3

        :param symbol: value to compare with values in the fields 1, 2 and 3
        :param element_1: value in field 1
        :param element_2: value in field 2
        :param element_3: value in field 3
        :return: boolean value. True if all values are the same False otherwise
        """
        return all((element_1 == symbol, element_2 == symbol, element_3 == symbol))

    def check_if_player_wins(self, symbol):
        """ checks if the player managed to reach 3 adjacent values horizontally, vertically or diagonally

        :param symbol: sign (symbol) the player inserts - should be the value from the scope ("X" or "O")
        :return: if the values in any row column or diagonal are equal, return True, False otherwise
        """
        if self.is_the_same_value(symbol, self.grid["1 1"], self.grid["1 2"], self.grid["1 3"]):
            return True
        elif self.is_the_same_value(symbol, self.grid["2 1"], self.grid["2 2"], self.grid["2 3"]):
            return True
        elif self.is_the_same_value(symbol, self.grid["3 1"], self.grid["3 2"], self.grid["3 3"]):
            return True
        elif self.is_the_same_value(symbol, self.grid["1 1"], self.grid["2 1"], self.grid["3 1"]):
            return True
        elif self.is_the_same_value(symbol, self.grid["1 2"], self.grid["2 2"], self.grid["3 2"]):
            return True
        elif self.is_the_same_value(symbol, self.grid["1 3"], self.grid["2 3"], self.grid["3 3"]):
            return True
        elif self.is_the_same_value(symbol, self.grid["1 1"], self.grid["2 2"], self.grid["3 3"]):
            return True
        elif self.is_the_same_value(symbol, self.grid["1 3"], self.grid["2 2"], self.grid["3 1"]):
            return True
        return False

    def check_if_any_player_wins(self, temp_list):
        x = self.check_if_player_wins("X")
        o = self.check_if_player_wins("O")

        if all((x, o)):
            return "Impossible"
        elif any((x, o)):
            return "X wins" if x else "O wins"
        else:
            return "Draw" if "_" not in Counter(temp_list).keys() else "Game not finished"

    def update_board(self, value: str):
        present = self.grid.get(value, False)

        if present:
            if present == "_":
                self.grid[value] = "X"
            else:
                return False, "This cell is occupied! Choose another one!"
        else:
            coordinates = value.split(" ")
            if not all([x in string.digits for x in coordinates]) or "" in coordinates:
                return False, "You should enter numbers!"
            else:
                return False, "Coordinates should be from 1 to 3!"
        return True, self.__str__()

    def make_move(self, symbol):
        move_status, msg = self.update_board(symbol)
        print(msg)
        while not move_status:
            current_move = input()
            move_status, msg = self.update_board(current_move)
            print(msg)

    def game_state(self):
        temp_list = self.return_as_list()
        if not self.check_count(temp_list):
            return "Impossible"
        return self.check_if_any_player_wins(temp_list)

    def __str__(self):
        msg = f"---------\n| {self.grid['1 1']} {self.grid['1 2']} {self.grid['1 3']} |\n" \
              f"| {self.grid['2 1']} {self.grid['2 2']} {self.grid['2 3']} |\n" \
              f"| {self.grid['3 1']} {self.grid['3 2']} {self.grid['3 3']} |\n" \
              "---------"

        return msg.replace("_", " ")


if __name__ == '__main__':
    user_input = input()
    game = GameInterface(*user_input)
    print(game)
    game.make_move(input())