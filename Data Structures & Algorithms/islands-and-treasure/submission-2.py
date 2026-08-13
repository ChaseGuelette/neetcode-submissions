class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()

        def addRoom(x, y):
            if (x == rows or 
            x < 0 or 
            y == cols or 
            y < 0 or 
            (x, y) in visited or 
            grid[x][y] == -1):
                return 
            visited.add((x, y))
            q.append((x, y))


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append([i, j])
                    visited.add((i, j))

        dist = 0
        while q:
            for i in range(len(q)):
                x,y = q.popleft()
                grid[x][y] = dist
                addRoom(x + 1, y + 0)
                addRoom(x + -1, y + 0)
                addRoom(x + 0, y + 1)
                addRoom(x + 0, y + -1)
            dist += 1 


        #I think this would work for me, but its too inefficent. I think because we have repeated work?? Not sure 
        # directions = [[1,0], [-1,0], [0,1],[0,-1]]

        # def dfs(x, y, dist, visited):
        #     #in grid and not water 
        #     if x >= len(grid) or x < 0 or y >= len(grid[0]) or y < 0 or grid[x][y] == -1:
        #         return 
            
        #     if (x, y) in visited:
        #         return 
            
        #     #do the work
        #     #how far from treasure? what is count
        #     #if its not a treasure item, then replace it with the max of its current value and the distance to the nearest treasure 
        #     if grid[x][y] > 0:
        #         grid[x][y] = min(dist, grid[x][y])
        #     visited.add((x,y))

            
        #     for direct in directions:
        #         dfs(x + direct[0], y + direct[1], dist + 1, visited)

        #     #return should be nothing since we are modifying in place
        #     visited.remove((x, y))
        #     return 
            

        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == 0:
        #             visited = set()
        #             dfs(i, j, 0, visited)
