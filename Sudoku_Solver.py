def empty(puzzle):
    for r in range(9):
        for c in range(9):
            if( puzzle[r][c] == 0):
                return r, c
    return None, None

def check(g, puzzle, r, c):
    # Row
    row_values = puzzle[r]
    if(g in row_values):
        return False
    # Column
    col_values = []
    for i in range(9):
        col_values.append(puzzle[i][c])
    if(g in col_values):
        return False
    # Box   
    row = (r // 3) * 3
    col = (c // 3) * 3
    for i in range(row, row + 3):
        for j in range(col, col + 3):
            if(puzzle[i][j] == g):
                return False
    return True

def solve(puzzle):
    r, c = empty(puzzle)
    if(r == None):
        return True
    for g in range(1, 10):
        if(check(g, puzzle, r, c)):
            puzzle[r][c] = g
            if(solve(puzzle)):
                return puzzle
        puzzle[r][c] = 0
    return False

def Print(puzzle):
    for i in puzzle:
        print(i)

p1 = [[0, 0, 0, 0, 0, 5, 0, 7, 0], [0, 0, 0, 0, 0, 0, 5, 0, 1], [8, 9, 0, 0, 0, 6, 0, 0, 0]]
p2 = [[7, 0, 0, 4, 3, 0, 2, 0, 0], [4, 0, 0, 9, 0, 2, 0, 0, 5], [0, 0, 2, 0, 7, 8, 0, 0, 3]]
p3 = [[0, 0, 0, 1, 0, 0, 0, 4, 2], [1, 0, 7, 0, 0, 0, 0, 0, 0], [0, 8, 0, 2, 0, 0, 0, 0, 0]]
puzzle = p1 + p2 + p3
solve(puzzle)
Print(puzzle)
