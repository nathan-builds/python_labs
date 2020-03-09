def give_change(amount, coins):

    sum = 0
    answer = []

    for coin in coins:
        while coin + sum <= amount:
            answer.append(coin)
            sum += coin

    return answer

print(give_change(100, [42, 17, 11, 6, 1]))