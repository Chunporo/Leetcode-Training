class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dp = [[0] * n for _ in range(m)]
        dp[startRow][startColumn] = 1
        result = 0

        for move in range(maxMove):
            dp_new = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    for dx, dy in directions:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < m and 0 <= nj < n:
                            dp_new[i][j] = (dp_new[i][j] + dp[ni][nj]) % MOD
                        else:
                            result = (result + dp[i][j]) % MOD
            dp = dp_new

        return result