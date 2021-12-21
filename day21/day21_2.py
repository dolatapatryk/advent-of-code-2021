def calculate_new_position(position, moves):
    new_position = position + moves
    return 10 if new_position%10==0 else new_position%10

def count(position1, score1, position2, score2, lookup):
    if score1 >= 21:
        return (1,0)
    if score2 >= 21:
        return (0,1)
    if (position1, score1, position2, score2) in lookup:
        return lookup[(position1, score1, position2, score2)]
    scores = (0,0)
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                new_position1 = calculate_new_position(position1, i+j+k)
                new_score1 = score1 + new_position1

                # calculate for second player
                x,y = count(position2, score2, new_position1, new_score1, lookup)
                scores = (scores[0] + y, scores[1] + x)
    lookup[(position1, score1, position2, score2)] = scores
    return scores

position1 = 7
position2 = 1
lookup = {}
print(count(position1, 0, position2, 0, lookup))