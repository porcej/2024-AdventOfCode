from math import sqrt, floor

def load_map(file_path):
    grid = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:  # Skip empty lines
                    grid.append(list(line))
        return grid

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except ValueError:
        print("Error: File contains non-numeric values or invalid format.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def part_one(map_grid):
    antinodes = set()
    antennas = {}
    max_rows = len(map_grid[0])
    max_cols = len(map_grid)
    for rdx, map_row in enumerate(map_grid):
        for cdx, point in enumerate(map_row):
            if point.isalnum():
                if point in antennas:
                    antennas[point].append((rdx,cdx))
                else:
                    antennas[point] = [(rdx,cdx)]

    for freq, points in antennas.items():
        while len(points) > 0:
            first_ant = points.pop(0)
            for second_ant in points:
                delta = tuple(x - y for x, y in zip(first_ant, second_ant))
                
                # Minus Side
                antinode = tuple(x + y for x, y in zip(first_ant, delta))
                if (0 <= antinode[0] < max_cols) and (0 <= antinode[1] < max_rows):
                    antinodes.add(antinode)
                
                # Plus Size
                antinode = tuple(x - y for x, y in zip(second_ant, delta))
                if (0 <= antinode[0] < max_cols) and (0 <= antinode[1] < max_rows):
                    antinodes.add(antinode)

    return antinodes



if __name__ == "__main__":
    file_path = "example.txt"
    file_path = "input.txt"

    map_grid = load_map(file_path)
    antinodes = part_one(map_grid)
    print(f'There are  {len(antinodes)}.')




