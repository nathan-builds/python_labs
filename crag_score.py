def crag_score(dice):
    point_score = 0

    if sum(dice) == 13:
        if dice.count(dice[0]) == 2 or dice.count(dice[1]) == 2 or dice.count(dice[2]) == 2:  # 6 6 1
            point_score = 50
    elif sum(dice) == 13:
        point_score = 26
    elif dice[0] == dice[1] and dice[1] == dice[2]:
        point_score = 25

    elif (1 in dice and 2 in dice and 3 in dice) or (4 in dice and 5 in dice and 6 in dice):
        point_score = 20
    elif (1 in dice and 3 in dice and 5 in dice) or (2 in dice and 4 in dice and 6 in dice):
        point_score = 20
    elif dice.count(6) >= 1:
        point_score = dice.count(6) * 6
    elif dice.count(5) >= 1:
        point_score = dice.count(5) * 5
    elif dice.count(4) >= 1:
        point_score = dice.count(4) * 4
    elif dice.count(3) >= 1:
        point_score = dice.count(3) * 3
    elif dice.count(2) >= 1:
        point_score = dice.count(2) * 2
    elif dice.count(1) >= 1:
        point_score = dice.count(1) * 1
    else:
        point_score = 0

    return point_score



