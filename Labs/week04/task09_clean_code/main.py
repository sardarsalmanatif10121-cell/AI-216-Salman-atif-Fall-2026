# main.py - Coordinates the prediction analysis workflow

from preprocessing import filter_by_confidence, split_complete_records, normalize_labels
from analysis import count_by_label, get_unique_labels, find_unexpected_labels, average_confidence, top_predictions

MIN_CONFIDENCE = 0.80
ALLOWED_LABELS = {"spam", "ham", "promotion"}
REQUIRED_FIELDS = ("id", "label", "confidence")
TOP_COUNT = 3

initial_predictions = [
    {"id": 1, "label": "spam", "confidence": 0.94},
    {"id": 2, "label": "ham", "confidence": 0.72},
    {"id": 3, "label": "promotion", "confidence": 0.41},
    {"id": 4, "label": "spam", "confidence": 0.89},
    {"id": 5, "label": "ham", "confidence": 0.97},
    {"id": 6, "label": "promotion", "confidence": 0.83},
    {"id": 7, "label": "ham", "confidence": 0.58}
]

new_batch = [
    {"id": 8, "label": "Spam", "confidence": 0.91},
    {"id": 9, "label": "ham"},
    {"id": 10, "label": "unknown", "confidence": 0.86},
    {"id": 11, "label": " HAM ", "confidence": 0.66}
]

# Part A
high_confidence = filter_by_confidence(initial_predictions, MIN_CONFIDENCE)
selected_ids = [p["id"] for p in high_confidence]
label_counts = count_by_label(initial_predictions)
unique_labels = sorted(get_unique_labels(initial_predictions))

print("=== Part A ===")
print(f"Selected IDs: {selected_ids}")
print(f"Label counts: {label_counts}")
print(f"Unique labels: {unique_labels}")

# Part B
all_predictions = initial_predictions + new_batch
complete, skipped_ids = split_complete_records(all_predictions, REQUIRED_FIELDS)
normalized = normalize_labels(complete)

summary = {
    "total_records": len(all_predictions),
    "valid_records": len(complete),
    "skipped_ids": skipped_ids,
    "labels": sorted(get_unique_labels(normalized)),
    "label_counts": count_by_label(normalized),
    "high_confidence_count": len(filter_by_confidence(normalized, MIN_CONFIDENCE)),
    "unexpected_labels": sorted(find_unexpected_labels(normalized, ALLOWED_LABELS)),
    "average_confidence": round(average_confidence(normalized), 3),
    "top_ids": top_predictions(normalized, TOP_COUNT)
}

print("\n=== Prediction Report ===")
print(f"Total records:          {summary['total_records']}")
print(f"Valid records:          {summary['valid_records']}")
print(f"Skipped (missing data): {summary['skipped_ids']}")
print(f"Labels:                 {summary['labels']}")
print(f"Label counts:           {summary['label_counts']}")
print(f"High confidence (>= 0.8): {summary['high_confidence_count']}")
print(f"Unexpected labels:      {summary['unexpected_labels']}")
print(f"Average confidence:     {summary['average_confidence']}")
print(f"Top 3 by confidence:   {summary['top_ids']}")

print(f"\nRecord 8 label in new_batch: {new_batch[0]['label']}")