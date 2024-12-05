# def get_diagonals(grid, word_length=0):
#     """
#     Extracts all diagonals from the grid as strings and returns them in a list.

#     :param grid: List of strings representing the grid.
#     :return: List of strings, where each string is a diagonal from the grid.
#     """
#     rows = len(grid)
#     cols = len(grid[0])
#     diagonals = ""

#     # Top-left to bottom-right diagonals
#     for d in range(word_length - 1, rows + cols - word_length):
#         for i in range(max(0, d - cols + 1), min(rows, d + 1)):
#             diagonals += grid[i][d - i]

#         diagonals += " "
#         for i in range(max(0, d - cols + 1), min(rows, d + 1)):
#             diagonals += grid[i][cols - 1 - (d - i)]

#         diagonals += " "

#     return diagonals


# # Given grid
# grid = [
#     "MMMSXXMASM",
#     "MSAMXMSMSA",
#     "AMXSXMAAMM",
#     "MSAMASMSMX",
#     "XMASAMXAMM",
#     "XXAMMXXAMA",
#     "SMSMSASXSS",
#     "SAXAMASAAA",
#     "MAMMMXMMMM",
#     "MXMXAXMASX",
# ]

# # Get diagonals as strings
# # diagonals = get_diagonals(grid, word_length=4)

# # # Print the result
# # print("Diagonals:")

# # print(diagonals)

# list_of_strings = ["abc", "def", "ghi"]

# transposed_list = "".join(list(zip(*list_of_strings)))
from math import floor
grid = [
    ["", "M", "", "S"],
    ["", "", "A", ""],
    ["", "M", "", "S"],
    ["", "", "", ""]
]

row_c = 3
row_r = 1

word = "MAM"
middle = floor(len(word)/2)
center_char = word[middle]

count = 0

for row_dx in range(middle-1, len(grid) - middle):
    for col_dx in range(middle-1, len(grid[row_dx]) - middle):
        
        # Check if we match the middle letter
        if grid[row_dx][col_dx] == center_char:
            loc = (row_dx, col_dx)

            diagonal_first =  f'{grid[row_dx-1][col_dx-1]}{center_char}{grid[row_dx+1][col_dx+1]}'
            diagonal_second = f'{grid[row_dx+1][col_dx-1]}{center_char}{grid[row_dx-1][col_dx+1]}'

            if diagonal_first == diagonal_second == word:
                count += 1
                print("Found")

            print(f'Checking {grid[row_dx][col_dx]} against {word[middle - 1]} at location {loc}.')
            print(f'\tDiagaonals: {diagonal_first} -- {diagonal_second}')


#         if grid[x][y] == center:
#             if grid[x-1][y-1] == 




# diagonal_lr = [grid[i][i] for i in range(len(word))]
# diagonal_rl = 
# print(diagonal)


print(" ")

# print(transposed_list)

# grid[x-1][y-1] grid[x][y] grid[x+1][y+1]
# grid[x-1][y+1] grid[x][y] grid[x+1][y-1]

# M.S
# .A.
# M.S

# M.M
# .A.
# S.S

# S.M
# .A.
# S.M

# S.S
# .A.
# M.M



