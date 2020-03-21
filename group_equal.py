def group_equal(items):
    temp_list = []
    final_list = []


    if not items:
        return []
    current_entry_in_list = items[0]

    for num in items:
        if num == current_entry_in_list:
            temp_list.append(current_entry_in_list)
        else:
            current_entry_in_list = num
            final_list.append(temp_list)
            temp_list=[]
            temp_list.append(num)

    final_list.append(temp_list)
    return final_list



print(group_equal([]))