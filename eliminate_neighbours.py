def eliminate_neighbours(new_list):
    new_list = list(new_list)

    max_number = max(new_list)
    number_of_operations = 0

    while max_number in new_list:
        smallest_number = min(new_list)

        if new_list.index(smallest_number) == 0:
            new_list.remove(new_list[1])
            number_of_operations += 1
            new_list.remove(smallest_number)


        elif new_list.index(smallest_number) == len(new_list) - 1:
            new_list.remove(new_list[len(new_list) - 1])
            number_of_operations += 1
            if len(new_list) == 1:  # added
                return number_of_operations
        else:
            neighbour_on_right = new_list[new_list.index(smallest_number) + 1]
            neighbour_on_left = new_list[new_list.index(smallest_number) - 1]

            if neighbour_on_right > neighbour_on_left:
                new_list.remove(neighbour_on_right)
            else:
                new_list.remove(neighbour_on_left)

            new_list.remove(smallest_number)

            number_of_operations += 1

    return number_of_operations


print(eliminate_neighbours([1000] + list(range(1, 1000))))