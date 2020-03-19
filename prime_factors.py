from math import sqrt


def prime_factors(n):
    if n == 0:  # catches edge case
        return [0]

    def is_prime(number_to_test):
        if (number_to_test <= 1):
            return False
        if (number_to_test == 2):
            return True
        if (number_to_test % 2 == 0):
            return False
        i = 3
        while i <= sqrt(number_to_test):
            if number_to_test % i == 0:
                return False
            i = i + 2

        return True

    def prime_generator(limit):
        a = 1
        while a < (limit / 2) + 100:  # this might not be large enough a number, check with tester
            a += 1
            if is_prime(a):
                yield a

    my_primes = prime_generator(n)

    factor_list = []
    factor = next(my_primes)

    while n != 1:
        if n % factor == 0:
            while n % factor == 0:
                factor_list.append(factor)
                n = n / factor
                if n % factor != 0:
                    factor = next(my_primes)

        else:
            factor = next(my_primes)

    return factor_list


print(prime_factors(10 ** 15 - 3))
