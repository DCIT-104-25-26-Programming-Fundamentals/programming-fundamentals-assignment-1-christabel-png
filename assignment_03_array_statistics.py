# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def calculate_sum(numbers):
    """Calculate the sum of a list of numbers."""
    total = 0
    for n in numbers:
        total += n
    return total

def Average(num):
    total = calculate_sum(num)
    return total / len(num)

def Maximum(num):
    maximum = num[0]
    for x in num:
        if x > maximum:
            maximum = x
    return maximum
def Minimum(num):
    minimum = num[0]
    for x in num:
        if x < minimum:
            minimum = x
    return minimum
def main():
    n = int(input("How many numbers? "))
    if n <= 0:
        print("Error: Number of elements must be a positive integer.")
        return

    numbers = []
    for i in range(n):
        number = float(input(f"Enter number {i + 1}: "))
        numbers.append(number)

    total_sum = calculate_sum(numbers)
    average = Average(numbers)
    maximum = Maximum(numbers)
    minimum = Minimum(numbers)

    def format_number(x):
        if isinstance(x, float) and x.is_integer():
            return str(int(x))
        return str(x)

    print("\nResults:")
    print(f"Sum:     {format_number(total_sum)}")
    print(f"Average: {format_number(average)}")
    print(f"Maximum: {format_number(maximum)}")
    print(f"Minimum: {format_number(minimum)}")
if __name__ == "__main__":
    main()
