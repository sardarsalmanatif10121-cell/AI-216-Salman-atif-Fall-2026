# Task 5 - Sets for Unique Labels & Validation

training_labels = ["spam", "ham", "spam", "promotion", "ham"]
test_labels = ["spam", "ham", "unknown", "promotion"]

# Convert to sets
training_set = set(training_labels)
test_set = set(test_labels)

# Unique training labels
print(f"Unique training labels: {sorted(training_set)}")

# Labels in both datasets
print(f"In both: {sorted(training_set & test_set)}")

# Labels only in test set
print(f"Only in test: {sorted(test_set - training_set)}")

# Labels in either dataset
print(f"In either: {sorted(training_set | test_set)}")