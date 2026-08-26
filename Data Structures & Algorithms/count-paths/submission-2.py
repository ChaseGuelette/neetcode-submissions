class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        store = [[0 for i in range(n)] for i in range(m)]
        store[0][0] = 1

        def dfs(r, c):
            if r >= m - 1 and c >= n - 1:
                return 1
            if r != 0 and c != 0 and store[r][c] != 0:
                return store[r][c]
            print(r, c)
            if r >= m - 1:
                store[r][c] = dfs(r, c + 1)
                return store[r][c]
            if c >= n - 1:
                store[r][c] = dfs(r + 1, c)
                return store[r][c]
            
            store[r][c] = dfs(r + 1, c) + dfs(r, c + 1) 
            return store[r][c]


        # dfs(1,0)
        # dfs(0,1)
        dfs(0,0)
        return store[0][0]

        