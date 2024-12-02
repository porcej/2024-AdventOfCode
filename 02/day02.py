def read_file(file_path, mapper=int):
    """
    Reads a file with two columns of numbers separated by spaces, stores each column in separate lists,
    and sorts them in ascending order.
    
    Args:
        file_path (str): The path to the text file.
        
    Returns:
        tuple: Two sorted lists, one for each column.
    """
    reports = []
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                levels = [mapper(level) for level in line.split()]
                reports.append(levels)
    
        return reports

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except ValueError:
        print("Error: File contains non-numeric values or invalid format.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def is_report_safe(report, min_diff=1, max_diff=3):
    increasing = False
    decreasing = False
    min_diff = 1
    max_diff = 3

    for ldx in range(len(report) - 1):
        difference = report[ldx] - report[ldx + 1]
        abs_difference = abs(difference)

        # is unsafe based on level difference thresholds
        if abs_difference < min_diff or abs_difference > max_diff:
            return False 

        if abs_difference == difference:
            increasing = True
        else:
            decreasing = True

        if increasing and decreasing:
            return False
    return True

def is_safe_with_damper(report, min_diff=1, max_diff=3):
    for ldx in range(len(report)):
        damped_report = report[:ldx] + report[ldx+1:]
        if is_report_safe(damped_report, min_diff, min_diff):
            return True
    return False



def part_one(reports):
    is_safe_count = 0

    for report in reports:
        is_safe = is_report_safe(report)
        if is_safe:
            is_safe_count += 1
        

    print(f'There are {is_safe_count} safe reports.')

def part_two(reports):
    is_safe_count = 0

    for report in reports:
        is_safe = is_safe_with_damper(report)
        if is_safe:
            is_safe_count += 1

    print(f'There are {is_safe_count} safe reports with damper.')



if __name__ == "__main__":
    
    # file_path = "part_1_example_input.txt"
    file_path = "part_1_input.txt"

    reports = read_file(file_path)
    part_one(reports)
    part_two(reports)

    # total_difference = part_one(column1, column2)
    # similarity_score = part_two(column1, column2)

    # if total_difference is not None:
    #     print(f'Total Difference: {total_difference}')
    #     print(f'Similarity Score: {similarity_score}')