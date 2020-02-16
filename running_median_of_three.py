def running_median_of_three(items):
    temp_list = []
    final_list = []
    beginning_of_sub_list = 0
    end_of_sub_list = 3

    if len(items) == 1:
        print(items)  ## just here for checking
        return items
    else:

        while end_of_sub_list <= len(items):
            temp_list = items[
                        beginning_of_sub_list:end_of_sub_list]  # creates temporary list to perform calculations on

            temp_list.sort()
            final_list.append(temp_list[1])  # adds the median item to the final list
            del (temp_list[0:3])
            beginning_of_sub_list += 1
            end_of_sub_list += 1

        final_list.insert(0, items[1])
        final_list.insert(0, items[0])

        print(final_list)  ## just here for checking
        return final_list


test_list = [1, 2, 3, 4, 5, 6, 7]

running_median_of_three(test_list)
