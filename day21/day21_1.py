def roll_dice(dice_side):
    moves = 0
    for _ in range(3):
        dice_side = (dice_side + 1)%100
        moves += dice_side
    return dice_side, moves

def calculate_new_position(position, moves):
    new_position = position + moves
    return 10 if new_position%10==0 else new_position%10

file = open('input.txt', 'r')

lines = [line.strip() for line in file.readlines()]
players_scores = {}
for line in lines:
    splitted = line.split(': ')
    position = int(splitted[1])
    player_no = int(splitted[0][7:9])
    # playerX: (position, actual_score)
    players_scores[player_no] = (position, 0)

dice_side = 0
rolls = 0
winner = None
while True:
    end = False
    for player in range(1,3):
        position, score = players_scores[player]
        dice_side, moves = roll_dice(dice_side)
        rolls += 3
        new_position = calculate_new_position(position, moves)
        score += new_position
        players_scores[player] = (new_position, score)
        if score >= 1000:
            winner = player
            end = True
            break
    if end:
        break
print(players_scores, rolls)

file.close()