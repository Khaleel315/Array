import sys

scores_str = sys.argv[1].replace(",", " ")
scores = list(map(int, scores_str.split()))

print("Sum =", sum(scores))
print("Average =", sum(scores) / len(scores))
print("Maximum =", max(scores))
print("Minimum =", min(scores))