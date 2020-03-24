def is_perfect_power(n):
    b = 2
    e = 1

    while b ** 2 <=n:

        if b ** e == n:
            return True
        elif b ** e < n:
            e += 1
        elif b ** e > n:
            b += 1
            e= 1

    return False


print(is_perfect_power(12**34))