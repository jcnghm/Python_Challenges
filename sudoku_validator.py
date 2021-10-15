# Sudoku Board Validator

from collections import defaultdict

def valid_solution(board):
    rows = defaultdict(int)
    columns = defaultdict(int)
    squares = defaultdict(int)
    for i in range(9):
        rows.clear()
        columns.clear()
        squares.clear()
        for j in range(9):
            if board[i][j] is not None:
                columns[board[i][j]] += 1
                if columns[board[i][j]]>1:
                    return False

            if board[j][i] is not None:
                rows[board[j][i]] += 1
                if rows[board[j][i]]>1:
                    return False
            new_j = (i*3 + j%3)%9
            new_i = (i//3)*3 + j//3
            if squares[board[new_i][new_j]] is not None:
                squares[board[new_i][new_j]] += 1
                if squares[board[new_i][new_j]]>1:
                    return False
    return True


# Test Board
valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2], 
                [6, 7, 2, 1, 9, 5, 3, 4, 8],
                [1, 9, 8, 3, 4, 2, 5, 6, 7],
                [8, 5, 9, 7, 6, 1, 4, 2, 3],
                [4, 2, 6, 8, 5, 3, 7, 9, 1],
                [7, 1, 3, 9, 2, 4, 8, 5, 6],
                [9, 6, 1, 5, 3, 7, 2, 8, 4],
                [2, 8, 7, 4, 1, 9, 6, 3, 5],
                [3, 4, 5, 2, 8, 6, 1, 7, 9]])