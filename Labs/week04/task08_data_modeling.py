# Task 8 - Choose the Right Data Structure

# Scenario A - List: model names in evaluation order
evaluated_models = ["resnet50", "inception_v3", "vit_base", "mobilenet"]
print(f"Scenario A - List: {evaluated_models}")

# Scenario B - Tuple: fixed image size
image_size = (224, 224)
print(f"Scenario B - Tuple: {image_size}")

# Scenario C - Dictionary: model with named fields
model_config = {
    "name": "spam_classifier",
    "threshold": 0.80,
    "version": 2,
    "debug": False
}
print(f"Scenario C - Dictionary: {model_config}")

# Scenario D - Set: unique class labels
unique_labels = {"spam", "ham", "promotion"}
print(f"Scenario D - Set: {sorted(unique_labels)}")

# Scenario E - List of Dictionaries: prediction records
predictions = [
    {"id": 1, "label": "spam", "confidence": 0.94},
    {"id": 2, "label": "ham", "confidence": 0.72},
    {"id": 3, "label": "promotion", "confidence": 0.83}
]
print(f"Scenario E - List of Dicts: {predictions}")

# Scenario F - Set: compare allowed vs received labels
allowed_labels = {"spam", "ham", "promotion"}
received_labels = {"spam", "ham", "unknown"}
unexpected = received_labels - allowed_labels
print(f"Scenario F - Unexpected labels: {sorted(unexpected)}")