class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[set() for _ in range(9)]
        columns=[set() for _ in range(9)]
        grid=[set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                num=board[row][col]
                if num=='.':
                    continue
                grid_indx=(row//3)*3+(col//3)
                if num in rows[row] or num in columns[col] or num in grid[grid_indx]:
                    return False
                rows[row].add(num)
                columns[col].add(num)
                grid[grid_indx].add(num)
        return True 


                
        