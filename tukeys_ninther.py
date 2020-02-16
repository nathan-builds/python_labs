

def tukeys_list(items):
    temp_list = []
    final_list = []

    while items:
        temp_list = items[0:3]  # creates temporary list to perform calculations on
        temp_list.sort()
        final_list.append(temp_list[1])  # adds the median item to the final list
        del (items[0:3])  # both delete statements clear the lists of the items that have already been used
        del (temp_list[0:3])
        # print(final_list)

    if len(final_list) == 1:
        print(final_list)
        return final_list
    else:
        tukeys_list(final_list)


check_list = [1, 5, 4, 75, 0, 99, 100, 245, 65]

print(tukeys_list(check_list))

# NEEDS  FIX: For some reason it returns None even though the function works, other than that NICE
