def disemvowel(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    final_string = ''
    previous_letter = 0
    next_letter = 2

    if text[0] == 'y':
        if text[1] not in vowels:
            final_string += text[0]
    else:
        final_string += text[0]

    for letter in text[1:]:
        if next_letter <= len(text):
            if letter == 'y':
                if text[previous_letter] not in vowels:
                    if text[next_letter] not in vowels:
                        final_string += letter
            else:
                final_string += letter

            previous_letter += 1
            next_letter += 1

    string_a = final_string.replace('a', '')
    string_e = string_a.replace('e', '')
    string_i = string_e.replace('i', '')
    string_o = string_i.replace('o', '')
    string_u = string_o.replace('u', '')

    return string_u
