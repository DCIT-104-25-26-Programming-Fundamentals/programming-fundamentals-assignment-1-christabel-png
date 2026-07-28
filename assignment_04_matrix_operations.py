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

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(str(x) for x in row))


def transpose_matrix():
    print("---Part A: Transpose Matrix---")
    try:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
    except ValueError:
        print("Invalid input. Please enter integers for rows and columns.")
        return

    matrix = []
    for i in range(1, rows + 1):
        row = list(map(int, input(f"Enter row {i}: ").split()))
        if len(row) != cols:
            print(f"Error: Expected {cols} values, got {len(row)}.")
            return
        matrix.append(row)

    transposed = [[matrix[r][c] for r in range(rows)] for c in range(cols)]

    print("Original Matrix:")
    print_matrix(matrix)
    print("Transposed Matrix:")
    print_matrix(transposed)


def add_matrices():
    print("\n---Part B: Add Two Matrices---")
    try:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
    except ValueError:
        print("Invalid input. Please enter integers for rows and columns.")
        return

    print("\nMatrix A:")
    matrix_a = []
    for i in range(1, rows + 1):
        row = list(map(int, input(f"Enter row {i} of Matrix A: ").split()))
        if len(row) != cols:
            print(f"Error: Expected {cols} values, got {len(row)}.")
            return
        matrix_a.append(row)

    print("\nMatrix B:")
    matrix_b = []
    for i in range(1, rows + 1):
        row = list(map(int, input(f"Enter row {i} of Matrix B: ").split()))
        if len(row) != cols:
            print(f"Error: Expected {cols} values, got {len(row)}.")
            return
        matrix_b.append(row)

    result = [[matrix_a[r][c] + matrix_b[r][c] for c in range(cols)] for r in range(rows)]
    print("Resultant Matrix (A + B):")
    print_matrix(result)


def multiply_matrices():
    print("\n---Part C: Multiply Two Matrices---")
    try:
        rows_a = int(input("Enter number of rows for Matrix A: "))
        cols_a = int(input("Enter number of columns for Matrix A: "))
    except ValueError:
        print("Invalid input. Please enter integers for rows and columns.")
        return

    matrix_a = []
    for i in range(1, rows_a + 1):
        row = list(map(int, input(f"Enter row {i} of Matrix A: ").split()))
        if len(row) != cols_a:
            print(f"Error: Expected {cols_a} values, got {len(row)}.")
            return
        matrix_a.append(row)

    try:
        rows_b = int(input("Enter number of rows for Matrix B: "))
        cols_b = int(input("Enter number of columns for Matrix B: "))
    except ValueError:
        print("Invalid input. Please enter integers for rows and columns.")
        return

    if rows_b != cols_a:
        print(f"Error: Number of rows in Matrix B ({rows_b}) must equal number of columns in Matrix A ({cols_a}).")
        return

    matrix_b = []
    for i in range(1, rows_b + 1):
        row = list(map(int, input(f"Enter row {i} of Matrix B: ").split()))
        if len(row) != cols_b:
            print(f"Error: Expected {cols_b} values, got {len(row)}.")
            return
        matrix_b.append(row)

    result = [[sum(matrix_a[r][k] * matrix_b[k][c] for k in range(cols_a)) for c in range(cols_b)] for r in range(rows_a)]
    print("Resultant Matrix (A x B):")
    print_matrix(result)


def main():
    transpose_matrix()
    add_matrices()
    multiply_matrices()


if __name__ == "__main__":
    main()
