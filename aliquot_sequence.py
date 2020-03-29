import functools

seen_items = {}


def aliquot_sequence(n, giveup):
    sequence = []
    sequence.append(n)
    temp_list = []
    a = n
    divisor = 1

    while len(sequence) <= giveup and 0 not in sequence:


            if a in seen_items:
                sequence.append(seen_items[a])
                a = seen_items[a]
                temp_list.clear()
                divisor = 1
            else:
                while divisor < a:
                    if a % divisor == 0:
                        temp_list.append(divisor)
                    divisor += 1

            list_sum = sum(temp_list)  # gets sum of list which is what we're looking for

            if list_sum in sequence:  # checks for value already appearing in sequence
                return sequence

            sequence.append(list_sum)  # adds it to list
            seen_items.update({a: list_sum})  # stores it in dictionary to recall later
            a = list_sum
            temp_list.clear()
            divisor = 1

    return sequence


