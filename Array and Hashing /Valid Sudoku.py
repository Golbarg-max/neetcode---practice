class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_list = []
        for i in board:
            for j in i: 
                if j != ".":
                    if j in row_list:
                        return False
                    else: 
                        row_list.append(j)
            row_list = []

        for col in range(9):
            seen = []
            for row in range(9):
                if board[row][col] != ".":
                    if board[row][col] in seen:
                        return False
                    seen.append(board[row][col])

        for box_row in [0, 3, 6]:
            for box_col in [0, 3, 6]:
                seen = []
                for i in range(box_row, box_row + 3):
                    for j in range(box_col, box_col + 3):
                        if board[i][j] != ".":
                            if board[i][j] in seen:
                                return False
                            seen.append(board[i][j])
        return True
