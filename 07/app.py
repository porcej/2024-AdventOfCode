def load_calibrations(file_path):
    """
    Reads a file and parses its contents into a dictionary.
    Each line in the file is expected to follow the format:
    key: value1 value2 value3 ...
    
    The key is an integer, and the values are a list of integers.

    :param file_path: Path to the input file
    :return: A dictionary with integer keys and list of integers as values
    """
    result = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:  # Skip empty lines
                    key, values = line.split(":")
                    result[int(key.strip())] = [v for v in values.strip().split()]
        return result

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except ValueError:
        print("Error: File contains non-numeric values or invalid format.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def make_equation(operands, operators):
    equation = ""
    for odx in range(len(operators)):
        equation = f'{equation}{operands[odx]}{operators[odx]}'
    equation += operands[-1]

    return equation

def perform_calulation(operands, operators):
    accumulator = int(operands[0])
    for odx, op in enumerate(operators):
        if op == '*':
            accumulator *= int(operands[odx + 1])
        elif op == '+':
            accumulator += int(operands[odx + 1])
        elif op == '||':
            accumulator = int(f'{accumulator}{operands[odx + 1]}')
    return accumulator



def cartesian_product(operators, repeat=1):
    """
    Compute the Cartesian product of multiple lists.

    :param operators: A list to compute the Cartesian product.
    :param repeat: Number of times to repeat lists
    :return: A list of tuples representing the Cartesian product.
    """
    if not operators:
        return [[]]  # Return a list with an empty list for an empty input
    lists = []
    for idx in range(repeat):
        lists.append(operators)

    # Recursive computation of Cartesian product
    result = [[]]
    for lst in lists:
        temp_result = []
        for x in result:
            for y in lst:
                temp_result.append(x + [y])
        result = temp_result
    return [tuple(x) for x in result]

def check_if_possible(resultant, operands, operators):
    num_operators = len(operands) - 1
    total_operator_possibilites = len(operators)**num_operators
    operator_combinations = cartesian_product(operators=operators, repeat=num_operators)
    for operator_combination in operator_combinations:
        # equation = make_equation(operands, operator_combination)
        # result = eval("".join(equation))
        result = perform_calulation(operands, operator_combination)
        if result == resultant:
            return True
    return False


def part_one(calibration_data):
    accumulator = 0
    for result, values in calibration_data.items():
        if check_if_possible(result, values, ["+", "*"]):
            accumulator += result
    return accumulator

def part_two(calibration_data):
    accumulator = 0
    for result, values in calibration_data.items():
        if check_if_possible(result, values, ["+", "*", "||"]):
            accumulator += result
    return accumulator

if __name__ == "__main__":
    file_path = "example.txt"
    file_path = "input.txt"

    calibration_data = load_calibrations(file_path)
    sum_valid_calibrations = part_one(calibration_data)
    print(f'The total calibration result is {sum_valid_calibrations}.')
    sum_valid_calibrations = part_two(calibration_data)
    print(f'The total calibration result with || is {sum_valid_calibrations}')



