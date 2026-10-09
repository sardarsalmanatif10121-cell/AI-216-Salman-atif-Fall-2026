# main.py - Import and use score_utils module

from score_utils import calculate_average, is_passing, count_above_threshold

scores = [72, 88, 45, 91, 67]

avg = calculate_average(scores)
print(f"Average: {avg:.2f}")
print(f"Is first score passing: {is_passing(scores[0])}")
print(f"Scores above 80: {count_above_threshold(scores, 80)}")