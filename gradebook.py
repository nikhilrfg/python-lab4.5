raw_scores = [85, 42, -10, 73, 59, 90, -5, 60]

passing_scores = []

for score in raw_scores:
    if score >= 60:
        passing_scores.append(score)

print("Passing scores: " + str(passing_scores))