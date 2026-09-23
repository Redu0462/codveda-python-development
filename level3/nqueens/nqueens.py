def solve_n_queens(n):
    solutions = []
    board = [-1] * n

    def is_safe(row, col):
        for r in range(row):
            c = board[r]
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True

    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    backtrack(0)
    return solutions

def print_solution(solution, n):
    for row in range(n):
        line = ""
        for col in range(n):
            line += "Q " if solution[row] == col else ". "
        print(line)
    print()

if __name__ == "__main__":
    n = int(input("Enter N (board size): "))
    solutions = solve_n_queens(n)
    print(f"Found {len(solutions)} solution(s) for N={n}\n")
    if solutions:
        print("First solution:")
        print_solution(solutions[0], n)