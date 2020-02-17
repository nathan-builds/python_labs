def winning_card(cards, trump):
    ranks = {'deuce': 2, 'two': 2, 'trey': 3, 'three': 3,
             'four': 4, 'five': 5, 'six': 6, 'seven': 7,
             'eight': 8, 'nine': 9, 'ten': 10, 'jack': 11,
             'queen': 12, 'king': 13, 'ace': 14}

    highest_trump = 0
    if trump is not None:

        for rank, suit in cards:
            if suit == trump and ranks[rank] > highest_trump:
                winning_card = (rank, suit)
                highest_trump = ranks[rank]

        return winning_card

    else:
        winning_card = cards[0]

        for rank, suit in cards[1:]:
            if suit == winning_card[1]:
                if ranks[rank] > ranks[winning_card[0]]:
                    winning_card = (rank, suit)

        return winning_card


my_var=winning_card([('ace', 'diamonds'), ('ace', 'hearts'), ('ace',
                                                       'spades'), ('deuce', 'clubs')], trump = 'clubs')

print(my_var)
