# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def addition(a, b):
    '''Returns the sum of two numbers.'''
    return a + b

def subtraction(a, b):
    '''Returns the difference of two numbers.'''
    return a - b

def multiplication(a, b):
    '''Returns the product of two numbers.'''
    return a * b

def division(a, b):
    '''Returns the quotient of two numbers.'''
    if b == 0:
        print("Error: Cannot divide by zero.")
        return None
    return round(a / b, 2)

def modulus(a, b):
    '''Returns the remainder of two numbers.'''
    if b == 0:
        print("Error: Cannot calculate modulus with zero.")
        return None
    return a % b

def exponentiation(a, b):
    '''Returns the result of raising a to the power of b.'''
    return a ** b
def display_menu():
    '''Displays the calculator menu.'''
    print("\n============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")
    return input("Select an operation (1-7): ")
def format_number(val_str):
    '''Attempts to convert a string to a float. Returns None if conversion fails.'''
    try:
        return float(val_str)
    except ValueError:
        print("Error: Invalid number entered.")
        return None

def main():
    '''Main function to run the calculator program.'''
    while True:
        choice = display_menu()
        if choice == '7':
            print("Goodbye!")
            break
        elif choice in {'1', '2', '3', '4', '5', '6'}:
            num1_str = input("Enter first number: ")
            num1 = format_number(num1_str)
            if num1 is None:
                continue
            num2_str = input("Enter second number: ")
            num2 = format_number(num2_str)
            if num2 is None:
                continue
            if choice == '1':
                result = addition(num1, num2)
                print(f"Result: {num1} + {num2} = {result}")
            elif choice == '2':
                result = subtraction(num1, num2)
                print(f"Result: {num1} - {num2} = {result}")
            elif choice == '3':
                result = multiplication(num1, num2)
                print(f"Result: {num1} * {num2} = {result}")
            elif choice == '4':
                result = division(num1, num2)
                if result is not None:
                    print(f"Result: {num1} / {num2} = {result}")
            elif choice == '5':
                result = modulus(num1, num2)
                if result is not None:
                    print(f"Result: {num1} % {num2} = {result}")
            elif choice == '6':
                result = exponentiation(num1, num2)
                print(f"Result: {num1} ** {num2} = {result}")
        else:
            print("Error: Invalid menu choice. Please select a number between 1 and 7.")

if __name__ == "__main__":
    main()