# score_utils.py - Reusable score utility functions

def calculate_average(scores):
    if len(scores) == 0:
        return None
    return sum(scores) / len(scores)

def is_passing(score, passing_score=50):
    return score >= passing_score

def count_above_threshold(scores, threshold):
    count = 0
    for score in scores:
        if score >= threshold:
            count += 1
    return count

if __name__ == "__main__":
    sample = [72, 88, 45, 91, 67]
    print("Demo from score_utils.py")
    print(f"Average: {calculate_average(sample):.2f}")
    print(f"Is 72 passing: {is_passing(72)}")
    print(f"Above 80: {count_above_threshold(sample, 80)}")