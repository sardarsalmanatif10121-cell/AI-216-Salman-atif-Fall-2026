# Task 5 - Debugging Challenge
# Original buggy code fixed with documented debugging process

# Bug 1: In calculate_average, total = score should be total += score
# Bug 2: In classify, condition order was wrong - >= 50 came before >= 85

def calculate_average(scores):
    total = 0
    for score in scores:
        total += score  # Fixed: was "total = score"
    return total / len(scores)

def classify(average):
    if average >= 85:      # Fixed: moved this condition before >= 50
        return "Excellent"
    elif average >= 50:
        return "Pass"
    else:
        return "Fail"

scores = [60, 70, 80, 90]

average = calculate_average(scores)
print("Average:", average)
print("Result:", classify(average))

# Debugging Notes:
# Expected output: Average: 75.0, Result: Pass
# Actual output (before fix): Average: 90 (only last value), Result: Pass
# Bug 1: total = score replaced total each time instead of adding
# Fix 1: changed to total += score
# Bug 2: classify returned "Pass" for 85+ scores because >= 50 came first
# Fix 2: moved >= 85 check before >= 50 check
# Corrected output: Average: 75.0, Result: Pass