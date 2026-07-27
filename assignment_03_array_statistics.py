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
    """Add up all the numbers in the list."""
    total = 0
    for number in numbers:
        total = total + number
    return total


def calculate_average(numbers):
    """Divide the total by how many numbers there are."""
    total = calculate_sum(numbers)
    average = total / len(numbers)
    return round(average, 2)


def find_maximum(numbers):
    """Find the biggest number in the list."""
    biggest = numbers[0]
    for number in numbers:
        if number > biggest:
            biggest = number
    return biggest


def find_minimum(numbers):
    """Find the smallest number in the list."""
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest


def read_numbers(how_many):
    """Ask the user for the numbers and put them in a list."""
    numbers = []
    for i in range(how_many):
        number = int(input(f"Enter number {i + 1}: "))
        numbers.append(number)
    return numbers


def main():
    count = int(input("How many numbers? "))

    if count <= 0:
        print("Error: N must be a positive integer.")
        return

    numbers = read_numbers(count)

    print()
    print("Results:")
    print("Sum:    ", calculate_sum(numbers))
    print("Average:", calculate_average(numbers))
    print("Maximum:", find_maximum(numbers))
    print("Minimum:", find_minimum(numbers))


main()

