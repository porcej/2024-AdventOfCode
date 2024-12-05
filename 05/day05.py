import re
from math import floor

def load_pages(file_path):
    """
    Reads a file with two columns of numbers separated by spaces, stores each column in separate lists,
    and sorts them in ascending order.
    
    Args:
        file_path (str): The path to the text file.
        
    Returns:
        tuple: Two sorted lists, one for each column.
    """
    page_order_rules = []
    updates = []
    modes = ['page ordering rules', 'update']
    mdx = 0
    try:
        with open(file_path, 'r') as file:
            for line in file:
            	line = line.strip()
            	if line == "":
            		mdx +=1
            		continue
            	if modes[mdx] == 'page ordering rules':
            		page_order_rules.append(tuple(map(int, line.split("|"))))
            	else:
	           		updates.append(list(map(int, line.split(","))))
        return (page_order_rules, updates)

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except ValueError:
        print("Error: File contains non-numeric values or invalid format.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def is_correct_order(update, page_order_rules):
    """Checks if an update is in the correct order based on the rules."""
    update_positions = {page: idx for idx, page in enumerate(update)}
    for first_num, second_num in page_order_rules:
        if first_num in update_positions and second_num in update_positions:
            if update_positions[first_num] > update_positions[second_num]:
                return False
    return True

def part_one(page_order_rules, updates):
	middle_number_page_sum = 0
	for update in updates:
		if is_correct_order(update, page_order_rules):
			middle_number_page_sum += update[len(update) // 2]

	return middle_number_page_sum


if __name__ == "__main__":
    
    file_path = "example.txt"
    file_path = "input.txt"

    page_order_rules, updates = load_pages(file_path)

    middle_page_sum_sorted = part_one(page_order_rules, updates)

    print(f'If you add up the middle page number from the correctly-ordered updates you will get {middle_page_sum_sorted}.')