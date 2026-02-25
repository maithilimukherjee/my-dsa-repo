class Solution:
    def nQueen(self, n):
        res = []
        
        def backtrack(row, sol):
            if row == n:
                # found a solution, convert to 1-indexed and store
                res.append([c+1 for c in sol])
                return
            
            for col in range(n):
                # check if placing queen at (row, col) is safe
                safe = True
                for r in range(row):
                    if sol[r] == col or abs(sol[r]-col) == abs(r-row):
                        safe = False
                        break
                if safe:
                    sol.append(col)
                    backtrack(row+1, sol)
                    sol.pop()
        
        backtrack(0, [])
        return res
