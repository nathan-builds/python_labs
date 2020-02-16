from operator import add


def safe_squares_knights(n, knights):
    board_size = n * n
    danger_squares = []
    knight_moves = [(2, 1), (1, 2), (2, -1), (-1, 2), (-2, 1), (1, -2), (-2, -1), (-1, -2)]
    new_list = [list(pair) for pair in knight_moves]
    new_knights_positions = [list(pair) for pair in knights]
    temp_list = []

    for pair in knights:
        i = 0
        while i < 8:
            temp_list = list(map(add, pair, new_list[i]))
            i += 1

            if temp_list[0] >= 0 and temp_list[0] < n:
                if temp_list[1] >= 0 and temp_list[1] < n:
                    if temp_list not in danger_squares:
                        danger_squares.append(temp_list)
    print(board_size - len(danger_squares) - len(new_knights_positions))


safe_squares_knights(100, [(row, (row * row) % 100) for row in range(100)])
