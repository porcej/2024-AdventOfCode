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
                grid.append(list(line.strip()))
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
            if position in objs:
                return (rdx, cdx)
    return None # No guard found


def patrol(map_grid, obstructions=['#']):
    # Find Guard who is represented by '^'
    guard = '^'
    guards = ['^', '>', 'V', '<']
    guard_move_vectors = {'^': (-1, 0), '>': (0, 1), 'V': (1, 0), '<': (0, -1)}
    guard_move_history = []
    distinct_positions = set()
    guard_position = find_object(map_grid, objs=[guard])
    if guard_position is not None:
        guard_row, guard_col = guard_position 
    # distinct_positions[f'{guard_row},{guard_col}'] = True
    while ((0 < guard_row < len(map_grid) - 1) and (0 < guard_col < len(map_grid[0]) -1)):
        distinct_positions.add((guard_row, guard_col))

        guard_move_vector = guard_move_vectors[guard]
        next_row, next_col = guard_row + guard_move_vector[0], guard_col + guard_move_vector[1]

        if map_grid[next_row][next_col] in obstructions:
            guard = guards[(guards.index(guard) +1) % 4]
        else:
            guard_row, guard_col = next_row, next_col

        distinct_positions.add((guard_row, guard_col))
        current_position = (guard_row, guard_col, guard)
        if current_position in guard_move_history:
            return None 
        else:
            guard_move_history.append(current_position)

    return distinct_positions


def part_one(map_grid, obstructions=['#']):
    distinct_positions = patrol(map_grid)
    return len(distinct_positions)


def part_two(map_grid):
    # First we narrow the field down by finding the distinct positions that 
    # The Guard touches because other locations will not have an impact
    count = 0
    n_count = 0
    distinct_positions = patrol(map_grid)
    for distinct_position in distinct_positions:
        row, col = distinct_position
        position_temp = map_grid[row][col]
        if position_temp in ['^', '>', '<', 'V']:
            continue
        map_grid[row][col] = '@'
        steps = patrol(map_grid, obstructions=['#', '@'])
        map_grid[row][col] = position_temp
        if steps is None:
            count += 1
    return count







    



if __name__ == "__main__":
    
    # file_path = "example.txt"
    file_path = "input.txt"
    map_grid = load_map_grid(file_path)
    num_distinct_positions = part_one(map_grid)
    print(f'The guard past through {num_distinct_positions} positions before leaving the area.')
    num_new_obstructions = part_two(map_grid)
    print(f'You can create a loop for the guard by placing obstructions in {num_new_obstructions} places.')

