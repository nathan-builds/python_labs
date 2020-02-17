def only_odd_digits(n):
    n = str(n)

    for digit in n:
        if int(digit) % 2 == 0:
            return False

    return True


print(only_odd_digits())