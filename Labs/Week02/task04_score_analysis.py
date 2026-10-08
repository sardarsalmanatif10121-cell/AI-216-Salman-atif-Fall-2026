# Input: list of model scores and threshold
# Processing: count above/below threshold, calculate average and percentage
# Output: summary of scores

scores = [0.72, 0.81, 0.88, 0.91, 0.67, 0.86, 0.79]
threshold = 0.85

if len(scores) == 0:
    print("No scores available.")
else:
    meeting_target = 0
    below_target = 0
    total = 0

    for score in scores:
        total += score
        if score >= threshold:
            meeting_target += 1
        else:
            below_target += 1

    average = total / len(scores)
    percentage = (meeting_target / len(scores)) * 100

    print(f"Meeting target (>= {threshold}): {meeting_target}")
    print(f"Below target: {below_target}")
    print(f"Average score: {average:.2f}")
    print(f"Percentage meeting target: {percentage:.2f}%")

# Why might this logic later be placed inside a reusable function?
# Because we may need to analyze different sets of scores with different
# thresholds repeatedly, and a function avoids repeating the same code.