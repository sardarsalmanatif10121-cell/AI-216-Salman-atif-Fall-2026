

# preprocessing.py - Data cleaning and filtering functions

def filter_by_confidence(predictions, min_confidence):
    return [p for p in predictions if p["confidence"] >= min_confidence]

def split_complete_records(predictions, required_fields):
    complete = []
    incomplete = []
    for record in predictions:
        if all(field in record for field in required_fields):
            complete.append(record)
        else:
            incomplete.append(record["id"])
    return complete, incomplete

def normalize_labels(predictions):
    normalized = []
    for record in predictions:
        new_record = record.copy()
        new_record["label"] = record["label"].strip().lower()
        normalized.append(new_record)
    return normalized