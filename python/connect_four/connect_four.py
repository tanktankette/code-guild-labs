class Board:
    def __init__(self, width=7, height=7):
        self.board = []
        self.turn = 1
        self.width = width
        self.height = height
        tmp = []
        for x in range(width):
            tmp = []
            for y in range(height):
                tmp.append("( )")
            self.board.append(tmp)

    def print_board(self):
        print("┌───┬───┬───┬───┬───┬───┬───┐")
        for i in range(self.height):
            print("│" + "│".join(self.get_row(i)) + "│")
            print("├───┼───┼───┼───┼───┼───┼───┤")
        print("│ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │")
        print("└───┴───┴───┴───┴───┴───┴───┘")

    def get_row(self, row):
        for i in range(self.width):
            yield self.board[i][row]

    def get_diagnal(self, row, orientation=0):
        column = 0
        if row >= self.height:
            column = row - self.height + 1
            row = self.height - 1
        r = min(self.height, self.width, row - column)
        for i in range(r + 1):
            x = row - i
            if orientation == 1:
                x = self.width - 1 - x
            yield self.board[x][column + i]

    def drop_token(self, column):
        if column < 0 or column > self.width - 1:
            raise ValueError
        elif self.board[column].count("( )") > 0:
            token = "(◯)"
            if self.turn % 2 == 0:
                token = "(◉)"
            row = self.height - self.board[column][::-1].index("( )") - 1
            self.board[column][row] = token
            self.turn += 1
            print(self.board[column][row])
            return self.check_victory()
        else:
            print("Column is full")
        return False

    def check_victory(self):
        for i in range(self.height):
            if "(◉)(◉)(◉)(◉)" in "".join(self.get_row(i)):
                return "◉"
            if "(◯)(◯)(◯)(◯)" in "".join(self.get_row(i)):
                return "◯"
        for c in self.board:
            if "(◉)(◉)(◉)(◉)" in "".join(c):
                return "◉"
            if "(◯)(◯)(◯)(◯)" in "".join(c):
                return "◯"
        for i in range(self.height + self.width - 1):
            c = "".join(self.get_diagnal(i, 0))
            if "(◉)(◉)(◉)(◉)" in c:
                return "◉"
            if "(◯)(◯)(◯)(◯)" in c:
                return "◯"
            c = "".join(self.get_diagnal(i, 1))
            if "(◉)(◉)(◉)(◉)" in c:
                return "◉"
            if "(◯)(◯)(◯)(◯)" in c:
                return "◯"
        return False


board = Board()
board.print_board()
victor = False
token = ""
while not victor:
    token = "(◯)"
    if board.turn % 2 == 0:
        token = "(◉)"
    try:
        victor = board.drop_token(int(input(f"{token}: Choose a column: "))-1)
    except ValueError:
        print("Not a valid column")
    board.print_board()

print(f"{victor} wins!")
