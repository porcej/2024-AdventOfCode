import re
from math import floor

def load_wordsearch_grid_from_file(file_path, normalize=True):
    """
    Reads a file with two columns of numbers separated by spaces, stores each column in separate lists,
    and sorts them in ascending order.
    
    Args:
        file_path (str): The path to the text file.
        
    Returns:
        tuple: Two sorted lists, one for each column.
    """
    grid = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if normalize:
                    line = line.upper()
                grid.append(line.strip())
        return grid

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except ValueError:
        print("Error: File contains non-numeric values or invalid format.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def find_word_in_string(text, word):
    """
    Counts the number of overlapping occurrences of a word in a string.

    :param text: The string to search in.
    :param word: The word to search for.
    :return: The number of overlapping occurrences of the word.
    """
    count = 0
    index = 0
    word_len = len(word)

    while index <= len(text) - word_len:
        # Check if the word matches at the current index
        if text[index:index + word_len] == word:
            count += 1
        index += 1  # Move forward by one character for overlapping matches

    return count

def get_diagonals(grid, word_length=0):
    """
    Extracts all diagonals from the grid as strings and returns them in a list.

    :param grid: List of strings representing the grid.
    :return: List of strings, where each string is a diagonal from the grid.
    """
    rows = len(grid)
    cols = len(grid[0])
    diagonals = ""

    # Top-left to bottom-right diagonals
    for d in range(word_length - 1, rows + cols - word_length):
        for i in range(max(0, d - cols + 1), min(rows, d + 1)):
            diagonals += grid[i][d - i]

        diagonals += " "
        for i in range(max(0, d - cols + 1), min(rows, d + 1)):
            diagonals += grid[i][cols - 1 - (d - i)]

        diagonals += " "

    return diagonals


def find_word_in_grid(grid, word, check_reverse=True):
    """
    Finds the given word in the grid in horizontal, vertical, or diagonal directions.
    :param grid: List of strings representing the grid.
    :param word: The word to search for.
    :return: List of starting positions and directions where the word is found.
    """
    word_length = len(word)
    horrizontal = " ".join(grid)


    # vertical = " ".join(columns = [''.join(row[i] for row in grid) for i in range(len(grid[0]))])
    transposed_list = [[string[i] for string in grid] for i in range(max(len(string) for string in grid))]

    transposted_strings = [''.join(tup) for tup in transposed_list]
    vertical = " ".join(transposted_strings)

    diagonals = get_diagonals(grid=grid, word_length=word_length)

    words = [word]
    if check_reverse:
        words.append(word[::-1])

    word_count = 0

    for c_word in words:

        word_count += find_word_in_string(horrizontal, c_word)
        word_count += find_word_in_string(vertical, c_word)
        word_count += find_word_in_string(diagonals, c_word)

    return word_count


def part_one(grid, word, normalize=True):
    if normalize:
        word = word.upper()
    return find_word_in_grid(grid, word)

def part_two(grid, word, normalize=True):
    if normalize:
        word = word.upper()

    middle = floor(len(word)/2)
    center_char = word[middle]

    words = [word, word[::-1]]
    # words = [word]

    count = 0

    print(f"Middle: {middle}, Middle -1: {middle-1}")
    for row_dx in range(middle, len(grid) - middle):
        print(f"ROW: {row_dx}")
        for col_dx in range(middle-1, len(grid[row_dx]) - middle):
            # print(f"COL: {col_dx}")
            
            # Check if we match the middle letter
            if grid[row_dx][col_dx] == center_char:
                diagonals = [
                    f'{grid[row_dx-1][col_dx-1]}{center_char}{grid[row_dx+1][col_dx+1]}',
                    f'{grid[row_dx-1][col_dx+1]}{center_char}{grid[row_dx+1][col_dx-1]}'
                 ]
                if (diagonals[0] in words) and  (diagonals[1] in words):
                    count += 1

    return count






if __name__ == "__main__":
    
    # file_path = "part_1_example_input.txt"
    file_path = "input.txt"
    # file_path = "input_one.txt"
    grid = load_wordsearch_grid_from_file(file_path)

    # Define the word to search
    word = "XMAS"
    word_count = part_one(grid, word)

    print(f'{word} was found {word_count} times.')

    grid2 = load_wordsearch_grid_from_file(file_path)
    word = "MAS"
    word__two_count = part_two(grid, word)
    print(f'X-{word} was found {word__two_count} times.')




    # part_one_result = part_one(memory)
    # part_two_result = part_two(memory)
    # print(f'Sum for operations:\n\t Part 1: {part_one_result}\n\t Part 2: {part_two_result}')



