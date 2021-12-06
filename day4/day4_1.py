from board import Board

file = open('input.txt', 'r')

# bingo numbers
numbers = [int(x) for x in file.readline().strip().split(',')]

# omit blank line
line = file.readline()

boards = []
actual_board = []
for line in file.readlines():
    line = line.strip()
    if line == '':
        board = Board(actual_board)
        boards.append(board)
        actual_board = []
        continue
    board_row = [int(x) for x in line.split(' ') if x != '']
    actual_board.append(board_row)
board = Board(actual_board)
boards.append(board)

last_number = None
counter = 0
winner_board = None
for number in numbers:
    last_number = number
    counter += 1
    for board in boards:
        board.update_board(number)
        if counter < 5:
            continue
        win = board.check_bingo()
        if win:
            winner_board = board
            break
    if winner_board is not None:
        break

sum_of_unmarked = winner_board.sum_of_unmarked()
result = last_number * sum_of_unmarked

print('result =', result)


file.close()