def reverse_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    list_of_vowels_in_text = []
    final_answer = ''

    for letter in text:
        if letter in vowels:
            list_of_vowels_in_text.append(letter)

    for letter in text:

        if letter in vowels:
            last_vowel = list_of_vowels_in_text[len(list_of_vowels_in_text) - 1]
            if letter.isupper():
                final_answer += last_vowel.upper()
            else:
                final_answer += last_vowel.lower()
            del list_of_vowels_in_text[len(list_of_vowels_in_text) - 1]
        else:
            if letter.isupper():
                final_answer += letter.upper()
            else:
                final_answer += letter.lower()

    return final_answer


print(reverse_vowels("Buonapartes. But I warn you, if you don't tell me that this means war"))

#expected  Baanepirtas. Bet E worn yuo, if yuo dan't till mu thet thas maons wur