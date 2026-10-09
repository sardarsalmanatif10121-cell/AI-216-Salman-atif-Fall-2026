# Input: obtained marks and total marks
# Processing: validate input, calculate percentage
# Output: percentage or error message

def calculate_percentage(obtained, total):
    if total <= 0:
        raise ValueError("Total marks must be greater than 0")
    if obtained < 0:
        raise ValueError("Obtained marks cannot be negative")
    if obtained > total:
        raise ValueError("Obtained marks cannot exceed total marks")
    return (obtained / total) * 100

def run_calculator():
    try:
        obtained = float(input("Enter obtained marks: "))
        total = float(input("Enter total marks: "))
        result = calculate_percentage(obtained, total)
    except ValueError as error:
        print(f"Error: {error}")
    else:
        print(f"Percentage: {result:.2f}%")
    finally:
        print("Calculation complete.")

run_calculator()