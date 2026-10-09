# Task 7 - enumerate() and zip()

# Part A - enumerate()
experiments = [0.81, 0.86, 0.79, 0.91]

print("Part A - enumerate():")
for index, score in enumerate(experiments, start=1):
    print(f"Experiment {index}: {score}")

# Part B - zip()
predictions = [True, False, True, True]
actual = [True, False, False, True]

print("\nPart B - zip():")
correct_count = 0

for predicted, actual_value in zip(predictions, actual):
    is_correct = predicted == actual_value
    if is_correct:
        correct_count += 1
    print(f"Predicted: {predicted} | Actual: {actual_value} | Correct: {is_correct}")

accuracy = correct_count / len(predictions)
print(f"\nAccuracy: {accuracy:.2f}")