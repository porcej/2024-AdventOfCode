import re
from collections import defaultdict, deque

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

def topological_sort(update, page_order_rules):
    """Sorts the pages according to the given rules using topological sorting."""
    graph = defaultdict(list)
    indegree = defaultdict(int)

    # Build the graph and indegree map
    for x, y in page_order_rules:
        if x in update and y in update:
            graph[x].append(y)
            indegree[y] += 1
            if x not in indegree:
                indegree[x] = 0

    # Initialize the queue with nodes that have no incoming edges
    queue = deque([node for node in update if indegree[node] == 0])
    sorted_pages = []

    # Perform topological sort
    while queue:
        current = queue.popleft()
        sorted_pages.append(current)
        for neighbor in graph[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_pages



def part_one(page_order_rules, updates):
	middle_page_sums = {
		'correct': 0,
		'incorrect': 0
	}
	for update in updates:

		# Part 1
		if is_correct_order(update, page_order_rules):
			middle_page_sums['correct'] += update[len(update) // 2]

		# Part 2
		else:
			updated_update = topological_sort(update, page_order_rules)
			middle_page_sums['incorrect'] += updated_update[len(updated_update) // 2]

	return middle_page_sums


if __name__ == "__main__":
    
    # file_path = "example.txt"
    file_path = "input.txt"

    page_order_rules, updates = load_pages(file_path)

    middle_page_sum = part_one(page_order_rules, updates)
    print(f'Middle Page Sums:\n\tCorrectly-ordered: {middle_page_sum['correct']}\n\tIncorrectly-ordered: {middle_page_sum['incorrect']}')