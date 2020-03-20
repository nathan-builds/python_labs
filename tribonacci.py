def tribonacci(n, start=(1, 1, 1)):
    sequence_list = list(start)
    counter = 2



    while counter <= n:
        sequence_list.append(sum(sequence_list))
        sequence_list.pop(0)
        counter += 1
        if counter == n:
            return int(sequence_list[2])


print(tribonacci(1000))