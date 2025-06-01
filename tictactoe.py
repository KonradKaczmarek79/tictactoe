from collections import Counter

class GameInterface:
    def __init__(self, a1, a2, a3, b1, b2, b3, c1, c2, c3):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3

    def return_as_list(self):
        return [self.a1, self.a2, self.a3, self.b1, self.b2, self.b3, self.c1, self.c2, self.c3]

    @staticmethod
    def check_count(temp_list):
        counts = Counter(temp_list)
        if abs(counts["X"] - counts["O"]) > 1:
            return False
        return True

    @staticmethod
    def is_the_same_value(symbol, element_1, element_2, element_3):
        return all((element_1 == symbol, element_2 == symbol, element_3 == symbol))

    def check_if_player_wins(self, symbol):
        if self.is_the_same_value(symbol, self.a1, self.a2, self.a3):
            return True
        elif self.is_the_same_value(symbol, self.b1, self.b2, self.b3):
            return True
        elif self.is_the_same_value(symbol, self.c1, self.c2, self.c3):
            return True
        elif self.is_the_same_value(symbol, self.a1, self.b1, self.c1):
            return True
        elif self.is_the_same_value(symbol, self.a2, self.b2, self.c2):
            return True
        elif self.is_the_same_value(symbol, self.a3, self.b3, self.c3):
            return True
        elif self.is_the_same_value(symbol, self.a1, self.b2, self.c3):
            return True
        elif self.is_the_same_value(symbol, self.a3, self.b2, self.c1):
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

    def game_state(self):
        temp_list = self.return_as_list()
        if not self.check_count(temp_list):
            return "Impossible"
        return self.check_if_any_player_wins(temp_list)

    def __str__(self):
        return f"---------\n| {self.a1} {self.a2} {self.a3} |\n" \
        f"| {self.b1} {self.b2} {self.b3} |\n" \
        f"| {self.c1} {self.c2} {self.c3} |\n" \
        "---------\n" \
        f"{self.game_state()}"


if __name__ == '__main__':
    user_input = input()
    game = GameInterface(*user_input)
    print(game)