def collapse_intervals(items):
    temp_list = []
    final_string = ''

    if not items:
        return ''

    if len(items) == 1:
        return str(items[0])

    temp_list.append(items[0])
    previous = items[0]

    for current in items[1:]:
        if current == previous + 1:
            temp_list.append(current)
            previous = current
        else:
            if len(temp_list) == 1:
                final_string += str(temp_list[0])
                final_string += ','
                temp_list = []
                temp_list.append(current)
                previous = current
            else:

                final_string += str(temp_list[0])
                final_string += '-'
                final_string += str(temp_list[len(temp_list) - 1])
                final_string += ','
                temp_list = []
                temp_list.append(current)
                previous = current

    if len(temp_list)==1:
        final_string += str(temp_list[0])
    else:

        final_string += str(temp_list[0])
        final_string += '-'
        final_string += str(temp_list[len(temp_list) - 1])

    return final_string


test = [42]

print(collapse_intervals((list(range(1, 1000001)))))
