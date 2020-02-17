def is_cyclops(n):
    count_of_zero = 0
    number_list = [int(x) for x in str(n)]
    print(number_list)

    for number in number_list:
        if number == 0:
            count_of_zero += 1
        print(count_of_zero)

    if count_of_zero == 1:
        if len(number_list) % 2 == 1:
            if (len(number_list[0:number_list.index(0)])) == (
                    len(number_list[number_list.index(0) + 1:])):  ## checks if two sublists from 0 in the middle are =
                return True
            else:
                return False
        else:
            return False

    else:
        return False


is_cyclops(98053)
