def is_ascending(items):
    i = 0
    for number in items[1:]:
        if number <= items[i]:
            return False
        else:
            i += 1

    return True



