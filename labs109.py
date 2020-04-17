import functools
import math
from operator import add
from math import sqrt


######################################################################
def riffle(items, out=False):
    final_list = []
    first_segment = items[:len(items) // 2]
    second_segment = items[len(items) // 2:]
    second_number_counter = 0

    if out:
        for first_num in first_segment:
            final_list.append(first_num)
            final_list.append(second_segment[second_number_counter])
            second_number_counter += 1

    else:
        for num in second_segment:
            final_list.append(num)
            final_list.append(first_segment[second_number_counter])
            second_number_counter += 1

    return final_list


######################################################################
seen_items = {}


def aliquot_sequence(n, giveup):
    sequence = []
    sequence.append(n)
    temp_list = []
    a = n
    divisor = 1

    while len(sequence) < giveup and 0 not in sequence:

        if a in seen_items:
            sequence.append(seen_items[a])
            a = seen_items[a]
            temp_list.clear()
            divisor = 1
        else:
            while divisor < a:
                if a % divisor == 0:
                    temp_list.append(divisor)
                divisor += 1

            list_sum = sum(temp_list)  # gets sum of list which is what we're looking for

            if list_sum in sequence:  # checks for value already appearing in sequence
                return sequence

            sequence.append(list_sum)  # adds it to list
            seen_items.update({a: list_sum})  # stores it in dictionary to recall later
            a = list_sum
            temp_list.clear()
            divisor = 1

    return sequence


# There could be a issue with finding duplicates which is when it should terminate, I may not have covered every situation

######################################################################

def is_ascending(items):
    i = 0
    for number in items[1:]:
        if number <= items[i]:
            return False
        else:
            i += 1

    return True


######################################################################
def bridge_hand_shape(hand):
    final_list = []
    new_hand = [rank[1] for rank in hand]

    final_list.append(new_hand.count("spades"))  # count method returns occurrence of each item in the list
    final_list.append(new_hand.count("hearts"))
    final_list.append(new_hand.count("diamonds"))
    final_list.append(new_hand.count("clubs"))

    return final_list


######################################################################

######################################################################
def crag_score(dice):
    point_score = 0
    dice_list = []
    if sum(dice) == 13:
        if dice.count(dice[0]) == 2 or dice.count(dice[1]) == 2 or dice.count(dice[2]) == 2:  # 6 6 1
            point_score = 50
            return point_score
        else:
            point_score = 26
            return point_score
    elif dice[0] == dice[1] and dice[1] == dice[2]:
        point_score = 25
        return point_score

    elif (1 in dice and 2 in dice and 3 in dice) or (4 in dice and 5 in dice and 6 in dice):
        point_score = 20
        return point_score
    elif (1 in dice and 3 in dice and 5 in dice) or (2 in dice and 4 in dice and 6 in dice):
        point_score = 20
        return point_score
    else:

        if dice.count(6) >= 1:
            point_score = dice.count(6) * 6
            dice_list.append(point_score)

        if dice.count(5) >= 1:
            point_score = dice.count(5) * 5
            dice_list.append(point_score)
        if dice.count(4) >= 1:
            point_score = dice.count(4) * 4
            dice_list.append(point_score)
        if dice.count(3) >= 1:
            point_score = dice.count(3) * 3
            dice_list.append(point_score)
        if dice.count(2) >= 1:
            point_score = dice.count(2) * 2
            dice_list.append(point_score)

        if dice.count(1) >= 1:
            point_score = dice.count(1) * 1
            dice_list.append(point_score)

        else:
            point_score = 0
    if dice_list:
        return max(dice_list)
    else:
        return 0


######################################################################
def domino_cycle(domino):
    if domino == []:
        return True
    else:

        i = 1
        if len(domino) == 1 and domino[0][0] == domino[0][1]:  # The occurence of a one tile list passed
            return True
        else:
            if domino[0][0] == domino[len(domino) - 1][1]:  # checks that the first and last tile are correct
                for pair in domino:
                    if i < len(domino):
                        if pair[1] == domino[i][0]:
                            i += 1

                        else:
                            return False
            else:
                return False

        return True


######################################################################
def double_until_all_digits(n, giveup=1000):
    counter = 0

    while counter <= giveup:
        my_list = [int(x) for x in str(n)]
        if 0 in my_list and 1 in my_list and 2 in my_list and 3 in my_list and 4 in my_list and 5 in my_list and 6 in \
                my_list and 7 in my_list and 8 in my_list and 9 in my_list:

            return counter

        else:
            n = n * 2
            counter += 1

    return -1


######################################################################

######################################################################
def expand_intervals(intervals):
    new_intervals = intervals.split(',')

    working_list = []
    answer = []

    for pair in new_intervals:
        temp = pair.split('-')
        working_list.append(temp)

    for number in working_list:
        if len(number) > 1:
            start = int(number[0])
            end = int(number[1])
            for x in range(start, end + 1):
                answer.append(x)
        else:
            answer.append(int(number[0]))

    return answer


######################################################################
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


######################################################################

def give_change(amount, coins):
    sum = 0
    answer = []

    for coin in coins:
        while coin + sum <= amount:
            answer.append(coin)
            sum += coin

    return answer


######################################################################

def hand_is_badugi(hand):
    rank = sorted([rank[0] for rank in hand])
    suit = sorted([suit[1] for suit in hand])
    if rank[0] == rank[1] or rank[1] == rank[2] or rank[2] == rank[
        3]:  # these are the only matches possible when list is sorted

        return False
    elif suit[0] == suit[1] or suit[1] == suit[2] or suit[2] == suit[3]:
        return False

    else:
        return True


######################################################################

def is_cyclops(n):
    count_of_zero = 0
    number_list = [int(x) for x in str(n)]

    for number in number_list:
        if number == 0:
            count_of_zero += 1

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


######################################################################

def iterated_remove_pairs(items):
    i = 1
    while True:
        if not items or len(items) == 1:
            return items

        if items[i - 1] == items[i]:
            del (items[i])
            del (items[i - 1])
            i = 1


        else:
            i += 1
            if i == len(items):
                return items

    return items


######################################################################

def md(a, b, n):
    counter = 0
    hash_test = {1: counter}
    counter += 1
    v = 1
    flag = True

    if v == n:
        return 1

    while flag:

        if v // a != 0 and v // a not in hash_test:
            hash_test.update({v // a: counter})
            v = v // a

        else:
            hash_test.update({b * v: counter})
            v = b * v

        counter += 1
        if v == n:
            return hash_test[v]


######################################################################

def milton_work_point_count(hand, trump):
    raw_point_count = 0
    for rank, suit in hand:
        if rank == 'ace':
            raw_point_count += 4
        if rank == 'king':
            raw_point_count += 3
        if rank == 'queen':
            raw_point_count += 2
        if rank == 'jack':
            raw_point_count += 1

    hand_shape = []
    new_hand = [rank[1] for rank in hand]
    hand_shape.append(new_hand.count("spades"))  # count method returns occurrence of each item in the list
    hand_shape.append(new_hand.count("hearts"))
    hand_shape.append(new_hand.count("diamonds"))
    hand_shape.append(new_hand.count("clubs"))

    hand_shape_dictionary = {"spades": hand_shape[0], 'hearts': hand_shape[1], 'diamonds': hand_shape[2],
                             'clubs': hand_shape[3]}

    if 4 in hand_shape:
        if hand_shape.count(3) == 3:  # checks if there are three suits with 3 cards in them ( is hand flat)
            raw_point_count -= 1

    for number in hand_shape:
        if number == 5:
            raw_point_count += 1
        if number == 6:
            raw_point_count += 2
        if number >= 7:
            raw_point_count += 3

    if trump != 'notrump':
        for key in hand_shape_dictionary:
            if hand_shape_dictionary[key] == 0 and key != trump:
                raw_point_count += 5

        for key in hand_shape_dictionary:
            if hand_shape_dictionary[key] == 1 and key != trump:
                raw_point_count += 3

    return raw_point_count


######################################################################

def only_odd_digits(n):
    n = str(n)

    for digit in n:
        if int(digit) % 2 == 0:
            return False

    return True


######################################################################


######################################################################

def pyramid_blocks(n, m, h):
    sum_total = 0

    while h:
        sum_total += n * m
        n += 1
        m += 1
        h -= 1
    return sum_total


######################################################################


def running_median_of_three(items):
    temp_list = []
    final_list = []
    beginning_of_sub_list = 0
    end_of_sub_list = 3

    if not items:
        return []

    if len(items) == 1:
        ## just here for checking
        return items
    else:

        while end_of_sub_list <= len(items):
            temp_list = items[
                        beginning_of_sub_list:end_of_sub_list]  # creates temporary list to perform calculations on

            temp_list.sort()
            final_list.append(temp_list[1])  # adds the median item to the final list
            del (temp_list[0:3])
            beginning_of_sub_list += 1
            end_of_sub_list += 1

        final_list.insert(0, items[1])
        final_list.insert(0, items[0])

        return final_list


######################################################################

def ryerson_letter_grade(n):
    if n < 50:
        return 'F'
    elif n > 89:
        return 'A+'
    elif n > 84:
        return 'A'
    elif n > 79:
        return 'A-'
    tens = n // 10
    ones = n % 10
    if ones < 3:
        adjust = "-"
    elif ones > 6:
        adjust = "+"
    else:
        adjust = ""
    return "DCB"[tens - 5] + adjust


######################################################################

def safe_squares_knights(n, knights):
    board_size = n * n
    danger_squares = []
    knight_moves = [(2, 1), (1, 2), (2, -1), (-1, 2), (-2, 1), (1, -2), (-2, -1), (-1, -2)]
    knight_moves_list = [list(pair) for pair in knight_moves]

    new_knights_positions = [list(pair) for pair in knights]
    for k in new_knights_positions:
        danger_squares.append(k)
    temp_list = []

    for pair in knights:
        i = 0
        while i < 8:
            temp_list = list(map(add, pair, knight_moves_list[i]))
            i += 1

            if temp_list[0] >= 0 and temp_list[0] < n:
                if temp_list[1] >= 0 and temp_list[1] < n:
                    if temp_list not in danger_squares:
                        danger_squares.append(temp_list)

    return board_size - len(danger_squares)


######################################################################

def safe_squares_rooks(n, rooks):
    columns = [x for x in range(0, n)]
    rows = [x for x in range(0, n)]

    for pairs in rooks:
        if pairs[0] in rows:
            rows.remove(pairs[0])
        if pairs[1] in columns:
            columns.remove(pairs[1])

    return len(columns) * len(rows)  ## just here for checking! one of test cases in PDF seems to fail


######################################################################

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


######################################################################

def taxi_zum_zum(moves):
    coordinates = [0, 0]
    direction = 'north'
    if type(moves) == str:
        for move in moves:
            if move == 'R' and direction == "north":
                direction = 'east'
            elif move == "R" and direction == "east":
                direction = 'south'
            elif move == 'R' and direction == 'south':
                direction = 'west'
            elif move == 'R' and direction == 'west':
                direction = 'north'
            elif move == 'L' and direction == 'north':
                direction = 'west'
            elif move == 'L' and direction == 'west':
                direction = 'south'
            elif move == 'L' and direction == 'south':
                direction = 'east'
            elif move == 'L' and direction == 'east':
                direction = 'north'
            elif move == 'F' and direction == 'north':
                coordinates[1] += 1
            elif move == 'F' and direction == 'south':
                coordinates[1] -= 1
            elif move == "F" and direction == 'east':
                coordinates[0] += 1
            elif move == 'F' and direction == 'west':
                coordinates[0] -= 1

        return tuple(coordinates)  # have to change this stupid return thing otherwise good to go !
    else:
        return tuple(coordinates)


######################################################################

def tukeys_ninthers(items):
    temp_list = []
    final_list = []

    while items:
        temp_list = items[0:3]  # creates temporary list to perform calculations on
        temp_list.sort()
        final_list.append(temp_list[1])  # adds the median item to the final list
        del (items[0:3])  # both delete statements clear the lists of the items that have already been used
        del (temp_list[0:3])

    if len(final_list) == 1:
        return final_list[0]
    else:

        return tukeys_ninthers(final_list)


######################################################################

def winning_card(cards, trump):
    ranks = {'deuce': 2, 'two': 2, 'trey': 3, 'three': 3,
             'four': 4, 'five': 5, 'six': 6, 'seven': 7,
             'eight': 8, 'nine': 9, 'ten': 10, 'jack': 11,
             'queen': 12, 'king': 13, 'ace': 14}
    winning_card = ()
    highest_trump = 0
    if trump is not None:

        for rank, suit in cards:
            if suit == trump and ranks[rank] > highest_trump:
                winning_card = (rank, suit)
                highest_trump = ranks[rank]

        if winning_card:
            return winning_card
        else:
            winning_card = cards[0]

        for rank, suit in cards[1:]:
            if suit == winning_card[1]:
                if ranks[rank] > ranks[winning_card[0]]:
                    winning_card = (rank, suit)

        return winning_card


    else:
        winning_card = cards[0]

        for rank, suit in cards[1:]:
            if suit == winning_card[1]:
                if ranks[rank] > ranks[winning_card[0]]:
                    winning_card = (rank, suit)

        return winning_card


######################################################################

def ztaloc(shape):
    collatz = []
    new_string = shape[::-1]
    current_value = 1
    for letter in new_string:

        if letter == 'd':
            current_value = current_value * 2
            collatz.append(current_value)
        elif letter == 'u':
            current_value = current_value // 3
            collatz.append(current_value)

    if collatz[len(collatz) - 1] == 0:
        return None
    else:
        return collatz[len(collatz) - 1]


######################################################################

def prime_factors(n):
    factor_list = []

    while n % 2 == 0:
        factor_list.append(2)
        n = n // 2

    for number in range(3, int(math.sqrt(n)) + 1, 2):

        while n % number == 0:
            factor_list.append(number)
            n = n // number

    if n > 2:
        factor_list.append(n)

    return factor_list

######################################################################

def tribonacci(n, start=(1, 1, 1)):
    sequence_list = list(start)
    counter = 2

    if n == 0:
        return sequence_list[0]
    elif n == 1:
        return sequence_list[1]
    elif n == 2:
        return sequence_list[2]

    else:

        while counter <= n:
            sequence_list.append(sum(sequence_list))
            sequence_list.pop(0)
            counter += 1
            if counter == n:
                return int(sequence_list[2])


######################################################################

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


######################################################################


###############################################################

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


######################################################################


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


######################################################################

def all_cyclic_shifts(text):
    final_list = []

    final_list.append(text)
    flag = True
    while flag:
        text += text[0]
        new_text = text[1:]
        text = new_text

        if new_text not in final_list:
            final_list.append(new_text)
        else:
            flag = False
    return sorted(final_list)


######################################################################

def group_equal(items):
    temp_list = []
    final_list = []

    if not items:
        return []
    current_entry_in_list = items[0]

    for num in items:
        if num == current_entry_in_list:
            temp_list.append(current_entry_in_list)
        else:
            current_entry_in_list = num
            final_list.append(temp_list)
            temp_list = []
            temp_list.append(num)

    final_list.append(temp_list)
    return final_list


######################################################################

def detab(text, n=8, sub='$'):
    final_string = ''
    count = 0
    for character in text:

        if character == '\t':
            final_string += sub
            count += 1
            while count % n != 0:
                final_string += sub
                count += 1
        else:
            final_string += character

            count += 1

    return final_string


######################################################################
def count_consecutive_summers(n):
    number_list = []
    final_count = 0

    start_of_sublist = 0
    end_of_sublist = 1

    for x in range(1, n + 1):
        number_list.append(x)

    while end_of_sublist < len(number_list):
        sublist_sum = sum(number_list[start_of_sublist:end_of_sublist])
        if sublist_sum == n:
            final_count += 1
            start_of_sublist += 1
            end_of_sublist = start_of_sublist + 1
        elif sublist_sum < n:
            end_of_sublist += 1
        elif sublist_sum > n:
            start_of_sublist += 1
            end_of_sublist = start_of_sublist + 1

    return final_count + 1


######################################################################
def is_perfect_power(n):
    b = 2
    e = 1

    while b ** 2 <= n:

        if b ** e == n:
            return True
        elif b ** e < n:
            e += 1
        elif b ** e > n:
            b += 1
            e = 1

    return False


######################################################################
def collapse_intervals(items):
    temp_list = []
    final_string = ''

    if not items:
        return ''

    if len(items) == 1:
        return str(items[0])

    temp_list.append(items[0])
    previous = items[0]

    for current in items[1:]:
        if current == previous + 1:
            temp_list.append(current)
            previous = current
        else:
            if len(temp_list) == 1:
                final_string += str(temp_list[0])
                final_string += ','
                temp_list = []
                temp_list.append(current)
                previous = current
            else:

                final_string += str(temp_list[0])
                final_string += '-'
                final_string += str(temp_list[len(temp_list) - 1])
                final_string += ','
                temp_list = []
                temp_list.append(current)
                previous = current

    if len(temp_list) == 1:
        final_string += str(temp_list[0])
    else:

        final_string += str(temp_list[0])
        final_string += '-'
        final_string += str(temp_list[len(temp_list) - 1])

    return final_string


######################################################################
def is_zigzag(n):
    n_as_string = str(n)

    if len(n_as_string) == 1:
        return True
    current_status = ''
    previous = int(n_as_string[1])

    first_sum = int(n_as_string[1]) - int(n_as_string[0])

    if first_sum > 0:
        current_status = 'positive'
    else:
        current_status = 'negative'

    for current in n_as_string[2:]:
        if int(current) - int(previous) > 0:
            if current_status == 'positive':
                return False
            else:
                if current_status == 'positive':
                    current_status = 'negative'
                elif current_status == 'negative':
                    current_status = 'positive'
        elif int(current) - int(previous) < 0:
            if current_status == 'negative':
                return False
            elif current_status == 'positive':
                current_status = 'negative'
        elif int(current) - int(previous) == 0:
            return False

        previous = current

    return True


######################################################################

def count_divisibles_in_range(start, end, n):
    if start == 0 and end == 0:
        return 1

    if start % n == 0:
        return ((end // n) - (start // n)) + 1

    return ((end // n) - (start // n))


######################################################################

def scrabble_value(word, multipliers):
    points_scored = 0
    scrabble_dict = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5,
                     'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4,
                     'w': 4, 'x': 8, 'y': 4, 'z': 10}
    count = 0
    if multipliers == None:
        for character in word:
            points_scored += scrabble_dict[character]
    else:

        for character in word:
            points_scored += scrabble_dict[character] * multipliers[count]
            count += 1

    return points_scored


######################################################################

word_shape_dict = {}


def words_with_given_shape(words, shape):
    letter_dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11,
                         'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21,
                         'v': 22,
                         'w': 23, 'x': 24, 'y': 25, 'z': 26}

    def build_key(letter_list):
        letter_string = ''
        for val in letter_list:
            letter_string += str(val)

        return letter_string

    if not word_shape_dict:
        final_list = []
        for word in words:
            previous_character = word[0]
            letter_shape = []
            for character in word[1:]:
                if letter_dictionary[character] > letter_dictionary[previous_character]:
                    letter_shape.append(1)
                elif letter_dictionary[character] < letter_dictionary[previous_character]:
                    letter_shape.append(-1)
                elif letter_dictionary[character] == letter_dictionary[previous_character]:
                    letter_shape.append(0)
                previous_character = character

            hash_key = build_key(letter_shape)

            if hash_key in word_shape_dict:

                word_shape_dict[hash_key].append(word)
            else:
                word_shape_dict.update({hash_key: [word]})

    else:
        answer_key = build_key(shape)

        if answer_key in word_shape_dict:
            return word_shape_dict[answer_key]
        else:
            return []

    return []


######################################################################

def reverse_ascending_sublists(items):
    temp_list = []
    final_list = []

    if not items:
        return []
    previous = items[0]
    temp_list.append(previous)

    for current in items[1:]:
        if current > previous:
            temp_list.append(current)

        else:
            for num in reversed(temp_list):
                final_list.append(num)
            temp_list = []
            temp_list.append(current)

        previous = current

    for num in reversed(temp_list):
        final_list.append(num)

    return final_list


######################################################################




def suppressed_digit_sum(n):
    if n == 1:
        return 0

    new_n = list(str(n))
    # print(new_n)
    temp_number = ''
    numbers_seen = set()
    counter = 0

    for number in new_n:

        temp_list = new_n.copy()
        del temp_list[counter]
        # print(temp_list)

        for num in temp_list:
            temp_number += num
            # print(temp_number)

        if int(temp_number) not in numbers_seen:
            numbers_seen.add(int(temp_number))

        temp_number = ''
        counter += 1

    return sum(numbers_seen)


######################################################################
def count_distinct_sums_and_products(items):
    seen_numbers = set()
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
                    seen_numbers.add(addition)
                if multiplication not in seen_numbers:
                    seen_numbers.add(multiplication)

    return len(seen_numbers)


######################################################################

def first_missing_positive(items):
    min_value = 1
    seen_numbers = set()

    for num in items:
        seen_numbers.add(num)

    while True:

        if min_value not in seen_numbers:
            return min_value
        else:
            min_value += 1


######################################################################
def is_permutation(items, n):
    number_dictionary = {}
    total_number_dictionary = {}
    set_of_items = set(items)

    number_set = {num for num in range(1, n + 1)}

    if set_of_items == number_set:
        return True
    else:
        return False


######################################################################


######################################################################
def remove_after_kth(items, k):
    count_dictionary = {}
    final_result = []
    for elem in items:
        count_dictionary.update({elem: 0})

    for elem in items:
        count_dictionary[elem] += 1
        if count_dictionary[elem] <= k:
            final_result.append(elem)

    return final_result


######################################################################
def words_with_letters(words, letters):
    answer_list = []

    for word in words:
        val = 0
        if letters[0] not in word or letters[1] not in word or letters[2] not in word:
            continue

        for letter in word:
            if letter == letters[val]:
                val += 1
                if val == len(letters):
                    answer_list.append(word)
                    break

    return answer_list


######################################################################
def bulgarian_solitaire(piles, k):
    numbers = [num for num in range(1, k + 1)]
    count = 0
    temp_list = []
    length = 0
    keep_going = True

    if sorted(piles) == numbers:
        return 0

    while keep_going:
        count += 1
        temp_list = []
        length = len(piles)
        for x in piles:
            if x != 1:
                temp_list.append(x - 1)

        temp_list.append(length)

        piles = temp_list

        set_temp_list = set(temp_list)
        for_counter = 0
        for num in numbers:
            for_counter += 1
            if num not in set_temp_list:
                break
            elif for_counter == len(numbers):
                keep_going = False

    return count


######################################################################
def create_zigzag(rows, cols, start):
    num_to_reach = start + (rows * cols) - 1
    section_count = cols
    running_count = start
    revolution_count = 0
    answer_list = []
    temp_list = []
    add_section_count = cols

    while revolution_count < rows:
        if revolution_count % 2 == 0:

            temp_list = [num for num in range(running_count, running_count + section_count)]
            answer_list.append(temp_list)
            revolution_count += 1
            running_count = temp_list[len(temp_list) - 1] + 1
            temp_list = []
        else:
            temp_list = [num for num in range(running_count, running_count + section_count)]
            revolution_count += 1
            running_count = temp_list[len(temp_list) - 1] + 1
            temp_list = temp_list[::-1]
            answer_list.append(temp_list)
            temp_list = []
    return answer_list


######################################################################
def bridge_hand_shorthand(hand):
    spades = []
    hearts = []
    diamonds = []
    clubs = []
    trial_dict = {'A': 0, 'K': 1, 'Q': 2, 'J': 3, 'x': 4, '-': 5}
    strl = ''

    for rank, suit in hand:
        if suit == 'clubs':
            if rank == "ace":
                clubs.append('A')
            elif rank == 'king':
                clubs.append('K')
            elif rank == 'queen':
                clubs.append('Q')
            elif rank == 'jack':
                clubs.append('J')
            else:
                clubs.append('x')

        elif suit == 'hearts':
            if rank == "ace":
                hearts.append('A')
            elif rank == 'king':
                hearts.append('K')
            elif rank == 'queen':
                hearts.append('Q')
            elif rank == 'jack':
                hearts.append('J')
            else:
                hearts.append('x')

        elif suit == 'spades':
            if rank == "ace":
                spades.append('A')
            elif rank == 'king':
                spades.append('K')
            elif rank == 'queen':
                spades.append('Q')
            elif rank == 'jack':
                spades.append('J')
            else:
                spades.append('x')

        elif suit == 'diamonds':
            if rank == "ace":
                diamonds.append('A')
            elif rank == 'king':
                diamonds.append('K')
            elif rank == 'queen':
                diamonds.append('Q')
            elif rank == 'jack':
                diamonds.append('J')
            else:
                diamonds.append('x')

    if len(spades) == 0:
        spades.append('-')

    if len(hearts) == 0:
        hearts.append('-')
    if len(clubs) == 0:
        clubs.append('-')
    if len(diamonds) == 0:
        diamonds.append('-')

    sorted_spades = sorted(spades, key=lambda x: trial_dict[x])
    sorted_hearts = sorted(hearts, key=lambda x: trial_dict[x])
    sorted_clubs = sorted(clubs, key=lambda x: trial_dict[x])
    sorted_diamonds = sorted(diamonds, key=lambda x: trial_dict[x])

    return strl.join(sorted_spades) + ' ' + strl.join(sorted_hearts) + ' ' + strl.join(
        sorted_diamonds) + ' ' + strl.join(
        sorted_clubs)


