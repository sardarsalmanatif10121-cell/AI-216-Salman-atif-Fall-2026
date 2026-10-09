# Task 2 - Aliasing vs Copying

import copy

# Part A - Observe aliasing problem
original_scores = [70, 80, 90]
processed_scores = original_scores
processed_scores.append(100)
print("Part A - Aliasing:")
print("Original:", original_scores)
print("Processed:", processed_scores)

# Part B - Fix with .copy()
original_scores = [70, 80, 90]
processed_scores = original_scores.copy()
processed_scores.append(100)
print("\nPart B - Shallow Copy:")
print("Original:", original_scores)
print("Processed:", processed_scores)

# Part C - Shallow copy with list of dictionaries
raw_predictions = [
    {"id": 1, "label": "Spam"},
    {"id": 2, "label": "HAM"}
]
shallow_copy = raw_predictions.copy()
shallow_copy[0]["label"] = "spam"
print("\nPart C - Shallow Copy Problem:")
print("Raw after shallow copy edit:", raw_predictions)

# Deep copy fix
raw_predictions = [
    {"id": 1, "label": "Spam"},
    {"id": 2, "label": "HAM"}
]
deep_copy = copy.deepcopy(raw_predictions)
deep_copy[0]["label"] = "spam"
print("\nPart C - Deep Copy Fix:")
print("Raw after deep copy edit:", raw_predictions)
print("Deep copy:", deep_copy)