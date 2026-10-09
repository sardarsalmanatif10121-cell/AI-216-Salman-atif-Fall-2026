# Task 2 - Scope & Hidden State

# Part A - Observe Scope
score = 90

def show_score():
    score = 70
    print("Inside function:", score)

show_score()
print("Outside function:", score)

# Part B - Refactor Hidden State
def is_qualified(score, threshold):
    return score >= threshold

# Test with three values
print("\n--- Qualification Tests ---")
print(f"Score 90, threshold 85: {is_qualified(90, 85)}")
print(f"Score 80, threshold 85: {is_qualified(80, 85)}")
print(f"Score 85, threshold 85: {is_qualified(85, 85)}")

# Reflection:
# Explicit parameters make functions easier to reuse and test because
# the function does not depend on any external variable. You can call
# it with any value without changing anything outside the function.