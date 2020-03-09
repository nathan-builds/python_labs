def ztaloc(shape):
    collatz = []
    new_string = shape[::-1]
    current_value = 1
    for letter in new_string:

        if letter == 'd':
            current_value = current_value * 2
            collatz.append(current_value)
        elif letter == 'u':
            current_value = current_value // 3
            collatz.append(current_value)

    if collatz[len(collatz)-1] == 0:
        return None
    else:
        return collatz[len(collatz)-1]

        print(collatz[len(collatz)-1])


print(ztaloc('d'))
