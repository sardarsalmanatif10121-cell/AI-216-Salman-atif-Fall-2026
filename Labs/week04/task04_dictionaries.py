


# Task 4 - Dictionaries for Structured Records

# Create dictionary
model = {
    "name": "spam_classifier",
    "version": 2,
    "accuracy": 0.92,
    "threshold": 0.80,
    "status": "evaluated"
}

# Print model name
print(f"Model name: {model['name']}")

# Update accuracy
model["accuracy"] = 0.94
print(f"Updated accuracy: {model['accuracy']}")

# Add new field
model["owner"] = "AI-216 Team"

# Read missing field with default
print(f"Dataset: {model.get('dataset', 'Not specified')}")

# Iterate through all key-value pairs
print("\nAll fields:")
for key, value in model.items():
    print(f"  {key}: {value}")

# Part B - Nested Dictionary
model["metrics"] = {
    "accuracy": 0.94,
    "precision": 0.91,
    "recall": 0.89
}

print(f"\nPrecision: {model['metrics']['precision']}")
print(f"Recall: {model['metrics']['recall']}")