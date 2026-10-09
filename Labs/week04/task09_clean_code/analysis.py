
# analysis.py - Analysis functions for predictions

def count_by_label(predictions):
    counts = {}
    for record in predictions:
        label = record["label"]
        if label not in counts:
            counts[label] = 0
        counts[label] += 1
    return counts

def get_unique_labels(predictions):
    return {record["label"] for record in predictions}

def find_unexpected_labels(predictions, allowed_labels):
    found_labels = get_unique_labels(predictions)
    return found_labels - allowed_labels

def average_confidence(predictions):
    if len(predictions) == 0:
        return None
    total = sum(p["confidence"] for p in predictions)
    return total / len(predictions)

def top_predictions(predictions, count):
    sorted_predictions = sorted(
        predictions,
        key=lambda p: p["confidence"],
        reverse=True
    )
    return [p["id"] for p in sorted_predictions[:count]]