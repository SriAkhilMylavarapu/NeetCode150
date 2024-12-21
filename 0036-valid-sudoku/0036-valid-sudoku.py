class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[0]*10 for i in range(9)]
        cols = [[0]*10 for i in range(9)]
        grids = [[[0]*10 for j in range(3)] for i in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = int(board[i][j])
                else:
                    continue
                if rows[i][num] == 1 or cols[j][num] == 1 or grids[i//3][j//3][num] == 1:
                    return False
                else:
                    rows[i][num] = 1
                    cols[j][num] = 1
                    grids[i//3][j//3][num] = 1
        return True
                
