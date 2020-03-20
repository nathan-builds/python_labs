def count_and_say(digits):

    temp_list = []
    final_list = []
    final_string = ''


    if not digits:
        return ' '
    else:
        current_number = digits[0]

        for num in digits:
            if num == current_number:
                temp_list.append(current_number)
            else:
                current_number = num
                final_list.append(len(temp_list))
                final_list.append(temp_list[0])
                temp_list.clear()
                temp_list.append(num)

        final_list.append(len(temp_list))
        final_list.append(temp_list[0])

        for number in final_list:
            final_string += str(number)

        return final_string


print(count_and_say(''))
