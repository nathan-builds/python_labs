def milton_work_point_count(hand, trump):
    raw_point_count = 0
    for rank, suit in hand:
        if rank == 'ace':
            raw_point_count += 4
        if rank == 'king':
            raw_point_count += 3
        if rank == 'queen':
            raw_point_count += 2
        if rank == 'jack':
            raw_point_count += 1

    hand_shape = []
    new_hand = [rank[1] for rank in hand]
    hand_shape.append(new_hand.count("spades"))  # count method returns occurrence of each item in the list
    hand_shape.append(new_hand.count("hearts"))
    hand_shape.append(new_hand.count("diamonds"))
    hand_shape.append(new_hand.count("clubs"))

    hand_shape_dictionary = {"spades": hand_shape[0], 'hearts': hand_shape[1], 'diamonds': hand_shape[2],
                             'clubs': hand_shape[3]}

    print(hand_shape)

    print(hand_shape_dictionary)

    if 4 in hand_shape:
        if hand_shape.count(3) == 3:  # checks if there are three suits with 3 cards in them ( is hand flat)
            raw_point_count -= 1

    for number in hand_shape:
        if number == 5:
            raw_point_count += 1
        if number == 6:
            raw_point_count += 2
        if number >= 7:
            raw_point_count += 3

    if trump != 'notrump':
        for number in hand_shape:
            if number == 0:
                raw_point_count += 5

    for key in hand_shape_dictionary:
        if hand_shape_dictionary[key] == 1 and key != trump:
            raw_point_count += 3

    print(raw_point_count)
    return raw_point_count
