# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 1
# Topic: Conditional Logic, Loops, and Functions
# =============================================================================
#
# TASK: Prime num Checker
#
# Write a Python program that checks whether a given num is prime.
#
# A prime num is a whole num greater than 1 that has no divisors
# other than 1 and itself (e.g., 2, 3, 5, 7, 11, 13 ...).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLES
# -----------------------------------------------------------------------------
#
#   Enter a num: 7
#   7 is a prime num.
#
#   Enter a num: 10
#   10 is NOT a prime num.
#
#   Enter a num: 1
#   1 is NOT a prime num.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement the logic inside a function (see scaffold below).
# - nums less than 2 are NOT prime — handle this inside the function.
# - The main block must call the function and print the result.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def is_prime(num):
    """Check if a whole num is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
            if num% i== 0:
                return False
    return True
def main():
    
    num = int(input("Enter a num: "))

    if is_prime(num):
        print(f"{num} is a prime num.")
    else:
        print(f"{num} is NOT a prime num.")

if __name__ == "__main__":
    main()