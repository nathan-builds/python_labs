def bridge_hand_shorthand(hand):
    spades = []
    hearts = []
    diamonds = []
    clubs = []
    trial_dict = {'A': 0, 'K': 1, 'Q': 2, 'J': 3, 'x': 4, '-': 5}
    strl = ''

    for rank, suit in hand:
        if suit == 'clubs':
            if rank == "ace":
                clubs.append('A')
            elif rank == 'king':
                clubs.append('K')
            elif rank == 'queen':
                clubs.append('Q')
            elif rank == 'jack':
                clubs.append('J')
            else:
                clubs.append('x')

        elif suit == 'hearts':
            if rank == "ace":
                hearts.append('A')
            elif rank == 'king':
                hearts.append('K')
            elif rank == 'queen':
                hearts.append('Q')
            elif rank == 'jack':
                hearts.append('J')
            else:
                hearts.append('x')

        elif suit == 'spades':
            if rank == "ace":
                spades.append('A')
            elif rank == 'king':
                spades.append('K')
            elif rank == 'queen':
                hearts.append('Q')
            elif rank == 'jack':
                spades.append('J')
            else:
                spades.append('x')

        elif suit == 'diamonds':
            if rank == "ace":
                diamonds.append('A')
            elif rank == 'king':
                diamonds.append('K')
            elif rank == 'queen':
                diamonds.append('Q')
            elif rank == 'jack':
                diamonds.append('J')
            else:
                diamonds.append('x')

    if len(spades) == 0:
        spades.append('-')
    elif len(hearts) == 0:
        hearts.append('-')
    elif len(clubs) == 0:
        clubs.append('-')
    elif len(diamonds) == 0:
        diamonds.append('-')

    sorted_spades = sorted(spades, key=lambda x: trial_dict[x])
    sorted_hearts = sorted(hearts, key=lambda x: trial_dict[x])
    sorted_clubs = sorted(clubs, key=lambda x: trial_dict[x])
    sorted_diamonds = sorted(diamonds, key=lambda x: trial_dict[x])

    print(sorted_clubs)
    print(sorted_diamonds)
    print(sorted_spades)
    print(sorted_hearts)

    print(
        strl.join(sorted_spades) + ' ' + strl.join(sorted_hearts) + ' ' + strl.join(sorted_diamonds) + ' ' + strl.join(
            sorted_clubs))


bridge_hand_shorthand([('trey', 'spades'), ('queen', 'hearts'), ('jack', 'hearts'),
                       ('eight', 'hearts'), ('six', 'diamonds'), ('nine',
                                                                  'diamonds'), ('jack', 'diamonds'), ('ace', 'diamonds'),
                       ('nine', 'clubs'), ('king', 'clubs'), ('jack', 'clubs'),
                       ('five', 'clubs'), ('ace', 'clubs')])