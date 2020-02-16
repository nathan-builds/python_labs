def riffle(items, out):
    my_dict = {}
    final_list = []
    list_position_counter = 0

    list_a = items[:len(items) // 2]  # Gets first half of list
    list_b = items[len(items) // 2:]  # Gets second half of list

    if out:
        for item in list_a:
            my_dict.update({item: list_b[list_position_counter]})  # creates pairs in dictionary from both lists
            list_position_counter += 1

    else:
        for item in list_b:
            my_dict.update({item: list_a[list_position_counter]})
            list_position_counter += 1

    for key in my_dict:
        final_list.append(key)
        final_list.append(my_dict[key])  # had to do this in two steps to create a single list

    return final_list


items = []

riffle(items, out=True)
