import sys

# LOCAL BRANCH FUNCTIONALITY:
# Sum + Average + Maximum + Minimum

if len(sys.argv) > 1:
    scores = sys.argv[1:]  # Read from system arguments
    print("User provided input values:")
else:
    print("No command-line input provided. Using default values:")
    scores = ["10", "20", "30", "40"]  # Default values

# Convert strings to integers
scores = [int(x) for x in scores]

# Perform calculations
total = sum(scores)
average = total / len(scores)
maximum = max(scores)
minimum = min(scores)

# Print results
print("Sum of scores =", total)
print("Average of scores =", average)
print("Maximum score =", maximum)
print("Minimum score =", minimum)
