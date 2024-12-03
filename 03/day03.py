import re

def load_memory_from_file(file_path):
    """
    Reads a file with two columns of numbers separated by spaces, stores each column in separate lists,
    and sorts them in ascending order.
    
    Args:
        file_path (str): The path to the text file.
        
    Returns:
        tuple: Two sorted lists, one for each column.
    """

    try:
        with open(file_path, 'r') as file:
            memory = file.read()
    
        return memory

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except ValueError:
        print("Error: File contains non-numeric values or invalid format.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



def perform_instruction(instruction):
    command, * values = instruction
    if command == 'mul':
        return int(values[0]) * int(values[1])



def part_one(memory_contents):
    register = 0
    instruction_pattern = r'(mul)\((\d+),(\d+)\)'
    instructions = re.findall(instruction_pattern, memory_contents)
    for instruction in instructions:
        print(instruction)
        register += perform_instruction(instruction)

    return register

def part_two(memory_contents):
    register = 0
    # Regular expressions to identify instructions
    mul_pattern = re.compile(r"mul\((\d+),(\d+)\)")
    do_pattern = re.compile(r"do\(\)")
    dont_pattern = re.compile(r"don't\(\)")

    command_enabled = True

    instruction_pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
    instructions = re.finditer(instruction_pattern, memory_contents)

    for instruction in instructions:
        token = instruction.group()

        if do_pattern.match(token):
            command_enabled = True
        elif dont_pattern.match(token):
            command_enabled = False
        else:
            if command_enabled:
                x, y = map(int, mul_pattern.match(token).groups())
                register += x * y
    return register

    



if __name__ == "__main__":
    
    # file_path = "example_input.txt"
    # file_path = "part_2_example_input.txt"
    file_path = "part_1_input.txt"

    memory = load_memory_from_file(file_path)
    print(memory)
    part_one_result = part_one(memory)
    part_two_result = part_two(memory)
    print(f'Sum for operations:\n\t Part 1: {part_one_result}\n\t Part 2: {part_two_result}')
