class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        if image[sr][sc] == color:
            return image

        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        def dfs(r, c, newColor, ogColor):
            #base case
            if (r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or 
        image[r][c] != ogColor):
                return 
            image[r][c] = newColor
            
            for dr, dc in directions: 
                dfs(r+dr, c+dc, newColor, ogColor)
            return
        
        dfs(sr, sc, color, image[sr][sc])
        return image

            
        