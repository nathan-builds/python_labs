def iterated_remove_pairs(items):
    i = 1
    while i < len(items) - 1:

        if items[i - 1] == items[i]:
            del (items[i - 1:i + 1])
            i = 1
        elif items[i + 1] == items[i]:
            del (items[i:i + 2])
            i = 1
        else:
            i += 1

    if items[0] == items[1]:
        items.clear()

    print(items)
