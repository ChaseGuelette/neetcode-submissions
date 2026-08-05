class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        seen = {}
        count = 0
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        def dfs(r, c):
            #base/invalid case (they're the same this time)
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or (r, c) in seen or grid[r][c] != '1':
                return 
            #do the work
            seen[(r,c)] = 1
            for dr, dc in directions:
                dfs(r+dr, c+dc)
            return 

        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                print("this is the current pair", (r,c))
                if grid[r][c] == '1' and (r, c) not in seen:
                    print("and we entered the loop!")
                    dfs(r, c)
                    count += 1
                print("And this is seen after the loop", seen)
        return count
    
        