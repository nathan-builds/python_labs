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
                final_answer += last_vowel
            del list_of_vowels_in_text[len(list_of_vowels_in_text) - 1]
        else:
            if letter.isupper():
                final_answer += letter.upper()
            else:
                final_answer += letter

    return final_answer


