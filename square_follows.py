import math

def square_follows(it):
    num_dict = {}
    final_answer = []
    numbers = it

    def generator(nums):
        for x in nums:
            yield x

    num_gen = generator(numbers)

    for number in num_gen:
        num_dict.update({number * number: ''})
        if number in num_dict and number != 1:
            final_answer.append(math.floor(math.sqrt(number)))

    return final_answer



