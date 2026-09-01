class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        import math
        valid_numbers = {"1", "2", "3","4","5","6","7","8","9"}

        cols = [set() for _ in range(9)]
        grids = [[set() for _ in range(3)] for _ in range(3)]

        for row_idx, row in enumerate(board):
            row_values = set()
            gridy_value = row_idx//3
            for col_idx, value in enumerate(row):
                if value == ".": continue

                gridx_value = col_idx//3
                if value not in valid_numbers or \
                value in row_values or \
                value in cols[col_idx] or \
                value in grids[gridx_value][gridy_value]: 
                    return False
                

                row_values.add(value)
                cols[col_idx].add(value)
                grids[gridx_value][gridy_value].add(value)
        return True
                

