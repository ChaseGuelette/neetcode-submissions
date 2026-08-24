class Solution:
    def countSubstrings(self, s: str) -> int:

        resIdx, resLen = 0, 0
        n = len(s)
        num = 0

        dp = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    num += 1
                    if resLen < (j - i + 1):
                        resIdx = i
                        resLen = j - i + 1

        return num
        