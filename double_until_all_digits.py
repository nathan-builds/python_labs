def double_until_all_digits(n, giveup):
    counter = 0

    while counter <= giveup:
        my_list = [int(x) for x in str(n)]
        if 0 in my_list and 1 in my_list and 2 in my_list and 3 in my_list and 4 in my_list and 5 in my_list and 6 in \
                my_list and 7 in my_list and 8 in my_list and 9 in my_list:

            return counter

        else:
            n = n * 2
            counter += 1

    return -1


print(double_until_all_digits(n=555, giveup=10))
