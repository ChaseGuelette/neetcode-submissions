class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        #this is the dfs solution1
        #I like this one better than the bfs. 
        seen = set()
        count = 0
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        def dfs(r, c):
            #base/invalid case (they're the same this time)
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or (r, c) in seen or grid[r][c] != '1':
                return 
            #do the work
            seen.add((r, c))
            for dr, dc in directions:
                dfs(r+dr, c+dc)
            return 

        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                if grid[r][c] == '1' and (r, c) not in seen:
                    dfs(r, c)
                    count += 1
        return count

                #okay this is the bfs solution 
        #dfs should be a bit different 
        # foundPos = {}
        # count = 0

        # def bfs(row, col):
        #     q = collections.deque()
        #     foundPos[(row, col)] = 1
        #     q.append((row, col))

        #     while q:
        #         r, c = q.popleft()
        #         directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        #         for dr, dc in directions:
        #             newR, newC = r + dr, c + dc

        #             if (newR in range(len(grid)) and
        #                 newC in range(len(grid[0])) and
        #                 grid[newR][newC] == "1" and
        #                 (newR, newC) not in foundPos):

        #                 q.append((newR, newC))
        #                 foundPos[(newR, newC)] = 1

        # for rows in range(len(grid)):
        #     for cols in range(len(grid[0])):
        #         if grid[rows][cols] == "1" and (rows, cols) not in foundPos:
        #             bfs(rows, cols)
        #             count += 1

        # return count
    
        