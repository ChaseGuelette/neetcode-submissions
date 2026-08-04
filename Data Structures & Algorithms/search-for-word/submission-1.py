class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        res = False
        directions = [[1,0], [-1,0], [0, 1], [0,-1]]

        def backtrack(r, c, wordIndex):
            if wordIndex == len(word):
                return True

            if (r<0 or r>=len(board) or c<0 or c>=len(board[0]) or board[r][c] != word[wordIndex]):
                return False

            temp = board[r][c]
            board[r][c] = "#"
            
            for direction in directions:
                if backtrack(r + direction[0], c + direction[1], wordIndex + 1):
                    return True

            board[r][c] = temp

            return False


        for i, row in enumerate(board):
            for j, letter in enumerate(row):
                if letter == word[0]:
                    res = backtrack(i, j, 0)
                    if res:
                        return True
        return res
        