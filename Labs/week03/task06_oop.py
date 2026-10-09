# Task 6 - ScoreAnalyzer Class

class ScoreAnalyzer:
    def __init__(self, scores):
        self.scores = scores

    def clean(self):
        self.scores = [s for s in self.scores if 0 <= s <= 100]

    def average(self):
        if len(self.scores) == 0:
            return None
        return sum(self.scores) / len(self.scores)

    def count_above(self, threshold):
        count = 0
        for score in self.scores:
            if score >= threshold:
                count += 1
        return count

    def summary(self):
        if len(self.scores) == 0:
            return {"count": 0, "average": None, "highest": None, "lowest": None}
        return {
            "count": len(self.scores),
            "average": self.average(),
            "highest": max(self.scores),
            "lowest": min(self.scores)
        }

# Test
raw_scores = [78, -5, 110, 67, 90, 88]
analyzer = ScoreAnalyzer(raw_scores)

print("Before clean:", analyzer.scores)
analyzer.clean()
print("After clean:", analyzer.scores)
print(f"Average: {analyzer.average():.2f}")
print(f"Above 80: {analyzer.count_above(80)}")
print(f"Summary: {analyzer.summary()}")