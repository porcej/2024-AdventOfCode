def read_and_sort_columns(file_path):
    """
    Reads a file with two columns of numbers separated by spaces, stores each column in separate lists,
    and sorts them in ascending order.
    
    Args:
        file_path (str): The path to the text file.
        
    Returns:
        tuple: Two sorted lists, one for each column.
    """
    column1 = []
    column2 = []
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Split the line by whitespace and convert to numbers
                numbers = line.split()
                if len(numbers) >= 2:  # Ensure there are at least two columns
                    column1.append(float(numbers[0]))
                    column2.append(float(numbers[1]))
        
        # Sort the columns
        column1.sort()
        column2.sort()
        
        return column1, column2

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except ValueError:
        print("Error: File contains non-numeric values or invalid format.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def part_one(column1, column2):
    """
    Computes the difference between sets of number by 
    
    Args:
        column1 (list(float)): First list of numbers
        column2 (list(float)): Second list of numbers
        
    Returns:
        float or None: The sum of the differences between each item in two lists or None if the list are not the same length
    """
    if len(column1) == len(column2):
        difference = [abs(a - b) for a, b in zip(column1, column2)]
        return sum(difference)
    else:
        None

def part_two(left_list, right_list):
    """
    Computes the difference between sets of number by 
    
    Args:
        left_list (list(float)): First list of numbers
        right_list (list(float)): Second list of numbers
        
    Returns:
        float or None: The sum of the differences between each item in two lists or None if the list are not the same length
    """
    
    counts = {idx: 0 for idx in left_list}
    print(counts)
    for idx in right_list:
        if idx in counts:
            counts[idx] += 1

    similarity_map =  {key: key * value for key, value in counts.items()}
    similarity = [similarity_map[idx] for idx in left_list]
    print("Similarity: ", similarity)
    return sum(similarity)






if __name__ == "__main__":
    
    # file_path = "example_input.txt" 
    # file_path = "part_2_example_input.txt"
    file_path = "input.txt"
    column1, column2 = read_and_sort_columns(file_path)

    total_difference = part_one(column1, column2)
    similarity_score = part_two(column1, column2)

    if total_difference is not None:
        print(f'Total Difference: {total_difference}')
        print(f'Similarity Score: {similarity_score}')


    
    
        # print("Column 1 (sorted):", sorted_column1)
        # print("Column 2 (sorted):", sorted_column2)
        # print("Difference       :", difference)
        # print(result)

