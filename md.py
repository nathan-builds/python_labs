def md(a, b, n):
    hash_test = {}
    v = 1
    flag = True

    if v == n:
        return 1

    while flag:

        if v // a != 0 and v // a not in hash_test:
            hash_test.update({v // a: ''})
            v = v // a
            if v == n:
                return len(hash_test) - 1

        else:
            hash_test.update({b * v: ''})
            v = b * v
            if v == n:
                return len(hash_test) - 1


print(md(3, 13, 231))  # expected result is 6

## having issue with 3,13,231
