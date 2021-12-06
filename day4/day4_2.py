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
last_winner = None
left_boards = boards
for number in numbers:
    last_number = number
    counter += 1
    if len(left_boards) == 1:
        last_winner = left_boards[0]
    for board in left_boards:
        board.update_board(number)
    if counter < 5:
        continue
    if last_winner is not None and last_winner.check_bingo():
        break
    left_boards = [board for board in left_boards if not board.check_bingo()]

sum_of_unmarked = last_winner.sum_of_unmarked()
result = last_number * sum_of_unmarked

print('result =', result)


file.close()