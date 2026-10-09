# Input: list of scores
# Processing: calculate average, find highest, count above threshold, classify
# Output: summary of scores

scores = [78, 85, 92, 67, 88]

def calculate_average(scores):
    if len(scores) == 0:
        return None
    return sum(scores) / len(scores)

def find_highest(scores):
    if len(scores) == 0:
        return None
    return max(scores)

def count_above_threshold(scores, threshold):
    count = 0
    for score in scores:
        if score >= threshold:
            count += 1
    return count

def classify_average(average):
    if average is None:
        return "No valid data"
    elif average >= 85:
        return "Excellent"
    elif average >= 70:
        return "Good"
    elif average >= 50:
        return "Satisfactory"
    else:
        return "Needs Improvement"

avg = calculate_average(scores)
highest = find_highest(scores)
above = count_above_threshold(scores, 80)
classification = classify_average(avg)

print(f"Scores: {scores}")
print(f"Average: {avg:.2f}")
print(f"Highest: {highest}")
print(f"Above 80: {above}")
print(f"Classification: {classification}")