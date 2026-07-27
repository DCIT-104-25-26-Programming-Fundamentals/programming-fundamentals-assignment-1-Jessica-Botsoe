# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def read_matrix(rows, columns, name):
    """Read a matrix from the user, one row on each line."""
    if name != "":
        print(f"Enter the values for matrix {name}:")

    matrix = []
    for i in range(rows):
        # split() breaks "1 2 3" into the list ["1", "2", "3"]
        parts = input(f"Enter row {i + 1}: ").split()

        row = []
        for part in parts:
            row.append(int(part))

        matrix.append(row)

    return matrix


def display_matrix(matrix, title):
    """Print the matrix as a grid, one row on each line."""
    print(title)
    for row in matrix:
        for value in row:
            # a tab keeps the columns lined up
            print(value, end="\t")
        print()


def transpose_matrix(matrix, rows, columns):
    """PART A - turn the rows into columns and the columns into rows."""
    result = []
    for i in range(columns):
        new_row = []
        for j in range(rows):
            new_row.append(matrix[j][i])
        result.append(new_row)

    return result


def add_matrices(matrix_a, matrix_b, rows, columns):
    """PART B - add the two matrices one position at a time."""
    result = []
    for i in range(rows):
        new_row = []
        for j in range(columns):
            new_row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(new_row)

    return result


def multiply_matrices(matrix_a, matrix_b, rows, shared, columns):
    """PART C - multiply an M x N matrix by an N x P matrix."""
    result = []
    for i in range(rows):
        new_row = []
        for j in range(columns):
            # add up row i of A times column j of B
            total = 0
            for k in range(shared):
                total = total + matrix_a[i][k] * matrix_b[k][j]
            new_row.append(total)
        result.append(new_row)

    return result


def part_a():
    print("=============================================")
    print("PART A - TRANSPOSE A MATRIX")
    print("=============================================")

    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))
    matrix = read_matrix(rows, columns, "")

    result = transpose_matrix(matrix, rows, columns)

    print()
    display_matrix(matrix, "Original Matrix:")
    print()
    display_matrix(result, "Transposed Matrix:")


def part_b():
    print()
    print("=============================================")
    print("PART B - ADD TWO MATRICES")
    print("=============================================")

    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))

    matrix_a = read_matrix(rows, columns, "A")
    matrix_b = read_matrix(rows, columns, "B")

    result = add_matrices(matrix_a, matrix_b, rows, columns)

    print()
    display_matrix(matrix_a, "Matrix A:")
    print()
    display_matrix(matrix_b, "Matrix B:")
    print()
    display_matrix(result, "Sum (A + B):")


def part_c():
    print()
    print("=============================================")
    print("PART C - MULTIPLY TWO MATRICES")
    print("=============================================")

    rows = int(input("Enter number of rows for matrix A (M): "))
    shared = int(input("Enter number of columns for A / rows for B (N): "))
    columns = int(input("Enter number of columns for matrix B (P): "))

    matrix_a = read_matrix(rows, shared, "A")
    matrix_b = read_matrix(shared, columns, "B")

    result = multiply_matrices(matrix_a, matrix_b, rows, shared, columns)

    print()
    display_matrix(matrix_a, "Matrix A:")
    print()
    display_matrix(matrix_b, "Matrix B:")
    print()
    display_matrix(result, "Product (A x B):")


def main():
    part_a()
    part_b()
    part_c()


main()

