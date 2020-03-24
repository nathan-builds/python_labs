def count_distinct_sums_and_products(items):
    seen_numbers = []
    if len(items) == 1:
        return 2
    elif not items:
        return 0
    else:

        for number in items:
            for num in items:
                addition = number + num
                multiplication = number * num
                if addition not in seen_numbers:
                    seen_numbers.append(addition)
                if multiplication not in seen_numbers:
                    seen_numbers.append(multiplication)

    return len(seen_numbers)

# Not sure if this will pass all the tests for example try [1,2]


print (count_distinct_sums_and_products([2,3,5,7,9,11]))