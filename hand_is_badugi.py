def hand_is_badugi(hand):
    rank = sorted([rank[0] for rank in hand])
    suit = sorted([suit[1] for suit in hand])
    if rank[0] == rank[1] or rank[1] == rank[2] or rank[2] == rank[3]:  # these are the only matches possible when list is sorted

        return False
    elif suit[0] == rank[1] or suit[1] == suit[2] or suit[2] == suit[3]:
        return False

    else:
        return True


hand_is_badugi([('queen', 'hearts'), ('six', 'diamonds'), ('deuce', 'spades'), ('jack', 'spades')])
