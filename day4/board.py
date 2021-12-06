class Board:
    def __init__(self, board_matrix):
        self.position = {}
        self.board = board_matrix
        self.bingo = {
            "row": [0, 0, 0, 0, 0],
            "col": [0, 0, 0, 0, 0]
        }

        self.set_positions_dictionary()
    
    def set_positions_dictionary(self):
        self.position = {self.board[i][j]:(i, j) for i in range(len(self.board)) for j in range(len(self.board[0]))}

    def update_board(self, number):
        if number in self.position:
            x, y = self.position[number]
            self.board[x][y] = 'X'
            self.update_bingo(x, y)

    def update_bingo(self, x, y):
        self.bingo['row'][x] += 1
        self.bingo['col'][y] += 1
    
    def check_bingo(self):
        return 5 in self.bingo['row'] or 5 in self.bingo['col']

    def sum_of_unmarked(self):
        total = 0
        for row in self.board:
            for value in row:
                if value != 'X':
                    total += value
        return total

    def __str__(self):
        result = ''
        for row in self.board:
            result += str(row) + '\n'
        return result
