def bridge_hand_shape(hand):
    final_list = []
    new_hand = [rank[1] for rank in hand]

    final_list.append(new_hand.count("spades")) # count method returns occurrence of each item in the list
    final_list.append(new_hand.count("hearts"))
    final_list.append(new_hand.count("diamonds"))
    final_list.append(new_hand.count("clubs"))

    return final_list


