
def formingMagicSquare(s):
    # Find the magic square cost:
    # These are all possible values for magic squares between 1 and 9
    magic_squares = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]], 
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]], 
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]], 
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
    ]
    costs_array = []
    for magic_square in magic_squares:
        total_cost = 0
        for i in range(3):
            for j in range(3):
                total_cost += abs(magic_square[i][j] - s[i][j])
        costs_array.append(total_cost)
    return min(costs_array)
    
