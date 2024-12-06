def load_map_grid(file_path):
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
                line = line.strip()
                row = list(line)
                grid.append(row)
        return grid

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except ValueError:
        print("Error: File contains non-numeric values or invalid format.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def find_object(map_grid, objs):
    if isinstance(objs, list):
        pass
    if isinstance(objs, tuple):
        pass
    else:
        object = [objs]

    for rdx, map_row in enumerate(map_grid):
        for cdx, position in enumerate(map_row):
            # print(map_grid[rdx][cdx])
            if position in objs:
                return (rdx, cdx)
    return None # No guard found


def part_one(map_grid):
    # Find Guard who is represented by '^'
    num_steps = 1   # We start at one since the starting position counts
    guard = '^'
    guards = ['^', '>', 'V', '<']
    obstructions = ['#']
    distinct_positions = {}
    guard_position = find_object(map_grid, objs=[guard])
    if guard_position is not None:
        guard_row, guard_col = guard_position 
    # distinct_positions[f'{guard_row},{guard_col}'] = True
    while ((0 < guard_row < len(map_grid) - 1) and (0 < guard_col < len(map_grid[0]) -1)):
        distinct_positions[f'{guard_row},{guard_col}'] = True
        if guard == '^':
            next_step_row = guard_row - 1
            if map_grid[guard_row - 1][guard_col] in obstructions:
                guard = '>'
            else:
                guard_row = guard_row - 1
        elif guard == 'V':
            if map_grid[guard_row + 1][guard_col] in obstructions:
                guard = '<'
            else:
                guard_row = guard_row + 1
        elif guard == '<':
            next_step_row = guard_col - 1
            if map_grid[guard_row][guard_col - 1] in obstructions:
                guard = '^'
            else:
                guard_col = guard_col - 1
        elif guard == '>':
            next_step_row = guard_col + 1
            if map_grid[guard_row][guard_col + 1] in obstructions:
                guard = 'V'
            else:
                guard_col = guard_col + 1
    distinct_positions[f'{guard_row},{guard_col}'] = True

    return len(distinct_positions)






    



if __name__ == "__main__":
    
    file_path = "example.txt"
    file_path = "input.txt"
    map_grid = load_map_grid(file_path)
    num_distinct_positions = part_one(map_grid)
    print(f'The guard past through {num_distinct_positions} before leaving the area.')

