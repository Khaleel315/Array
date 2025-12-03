# ABC Branch Code
# Calculates sum, average, maximum, and minimum of scores
# Jenkins-friendly version (no input())

import sys

# Check if scores are passed
if len(sys.argv) < 2:
    print("Error: No scores provided. Pass scores like:")
    print('python array_score.py "10 20 30 40"')
    sys.exit(1)

# Read scores from command-line argument
scores = list(map(int, sys.argv[1].split()))

total = sum(scores)
average = total / len(scores)
maximum = max(scores)
minimum = min(scores)

print("Sum =", total)
print("Average =", average)
print("Maximum =", maximum)
print("Minimum =", minimum)