def extract_increasing(digits):
    final_list = []
    final_list.append(int(digits[0]))
    number_builder = ''

    for num in digits[1:]:
        number_builder += num
        if int(number_builder) > max(final_list):
            final_list.append(int(number_builder))
            number_builder = ''


    return final_list
