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


def add(first, second):
    """Add the two numbers together."""
    answer = first + second
    return answer


def subtract(first, second):
    """Take the second number away from the first one."""
    answer = first - second
    return answer


def multiply(first, second):
    """Multiply the two numbers."""
    answer = first * second
    return answer


def divide(first, second):
    """Divide the first number by the second one."""
    answer = first / second
    return round(answer, 2)


def modulus(first, second):
    """Find the remainder when the first number is divided by the second."""
    answer = first % second
    return answer


def power(first, second):
    """Raise the first number to the power of the second one."""
    answer = first ** second
    return answer


def display_menu():
    """Print the calculator menu."""
    print()
    print("============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


def main():
    while True:
        display_menu()
        choice = input("Select an operation (1-7): ")

        if choice == "7":
            print("Goodbye!")
            break

        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Error: Invalid choice. Please enter a number from 1 to 7.")
            continue

        first = int(input("Enter first number : "))
        second = int(input("Enter second number: "))

        if choice == "1":
            answer = add(first, second)
            print(f"Result: {first} + {second} = {answer}")

        elif choice == "2":
            answer = subtract(first, second)
            print(f"Result: {first} - {second} = {answer}")

        elif choice == "3":
            answer = multiply(first, second)
            print(f"Result: {first} * {second} = {answer}")

        elif choice == "4":
            # we cannot divide a number by zero
            if second == 0:
                print("Error: Cannot divide by zero.")
            else:
                answer = divide(first, second)
                print(f"Result: {first} / {second} = {answer}")

        elif choice == "5":
            if second == 0:
                print("Error: Cannot divide by zero.")
            else:
                answer = modulus(first, second)
                print(f"Result: {first} % {second} = {answer}")

        elif choice == "6":
            answer = power(first, second)
            print(f"Result: {first} ** {second} = {answer}")


main()

