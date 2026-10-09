# Input: list of accuracy scores
# Processing: slice, append, extend, replace, sort, count
# Output: various list operations results

accuracies = [0.82, 0.91, 0.87, 0.78, 0.93, 0.85]
THRESHOLD = 0.85

print(f"First: {accuracies[0]}")
print(f"Last: {accuracies[-1]}")
print(f"Middle four: {accuracies[1:5]}")

accuracies.append(0.89)
accuracies.extend([0.84, 0.90])

pos = accuracies.index(0.78)
accuracies[pos] = 0.80

print(f"Updated: {accuracies}")

count = sum(1 for s in accuracies if s >= THRESHOLD)
print(f"Scores >= {THRESHOLD}: {count}")
print(f"Highest: {max(accuracies)}")
print(f"Lowest: {min(accuracies)}")

sorted_scores = sorted(accuracies, reverse=True)
print(f"Sorted (high to low): {sorted_scores}")
print(f"Original order kept: {accuracies}")