# 36. Valid Sudoku

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dicts=[{} for _ in range(9)]
        col_dicts=[{} for _ in range(9)]
        box_dicts=[{} for _ in range(9)]
             
        for i in range(0,9): 
            for j in range(0,9):
                if board[i][j]==".":
                    continue
                if board[i][j] not in row_dicts[i]:
                    row_dicts[i][board[i][j]]=1
                else:
                    return False
                if board[i][j] not in col_dicts[j]:
                    col_dicts[j][board[i][j]]=1
                else:
                    return False
                if i<3 and j<3:
                    if board[i][j] not in box_dicts[0]:
                        box_dicts[0][board[i][j]]=1
                    else:
                        return False
                if i<3 and 3<=j<6:
                    if board[i][j] not in box_dicts[1]:
                        box_dicts[1][board[i][j]]=1
                    else:
                        return False
                if i<3 and 6<=j<9:
                    if board[i][j] not in box_dicts[2]:
                        box_dicts[2][board[i][j]]=1
                    else:
                        return False
                if 3<=i<6 and j<3:
                    if board[i][j] not in box_dicts[3]:
                        box_dicts[3][board[i][j]]=1
                    else:
                        return False
                if 3<=i<6 and 3<=j<6:
                    if board[i][j] not in box_dicts[4]:
                        box_dicts[4][board[i][j]]=1
                    else:
                        return False
                if 3<=i<6 and 6<=j<9:
                    if board[i][j] not in box_dicts[5]:
                        box_dicts[5][board[i][j]]=1
                    else:
                        return False
                if 6<=i<9 and j<3:
                    if board[i][j] not in box_dicts[6]:
                        box_dicts[6][board[i][j]]=1
                    else:
                        return False
                if 6<=i<9 and 3<=j<6:
                    if board[i][j] not in box_dicts[7]:
                        box_dicts[7][board[i][j]]=1
                    else:
                        return False
                if 6<=i<9 and 6<=j<9:
                    if board[i][j] not in box_dicts[8]:
                        box_dicts[8][board[i][j]]=1
                    else:
                        return False

        return True

