def pyramid_blocks(n, m, h):
    sum_total = 0

    while h:
        sum_total += n * m
        n += 1
        m += 1
        h -= 1

        print(sum_total)  ## just for checking


pyramid_blocks(10 ** 6, 10 ** 6, 10 ** 6)  ## just for checking
