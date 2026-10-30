class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
 

        # the third step is tricky to code, but we can do it simply. 
        # make the key of the hash set (r//3, c//3)
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set) 
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if ((board[r][c] in rows[r]) or
                    (board[r][c] in cols[c]) or
                    (board[r][c] in squares[(r // 3, c // 3)])):
                    
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True