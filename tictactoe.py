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

    def __str__(self):
        return f"{self.a1} {self.a2} {self.a3}\n" \
        f"{self.b1} {self.b2} {self.b3}\n" \
        f"{self.c1} {self.c2} {self.c3}"


if __name__ == '__main__':
    game = GameInterface(*"XOXOXOXXO")
    print(game)
