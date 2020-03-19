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
            for x in range(start, end+1):
                answer.append(x)
        else:
            answer.append(int(number[0]))

    return answer







