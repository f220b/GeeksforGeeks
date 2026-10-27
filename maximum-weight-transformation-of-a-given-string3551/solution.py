class Solution:
    def getMaxWeight(self, s):
        n = len(s)
        if n == 0:
            return 0
        prev2, prev1 = 0, 1          # dp[0], dp[1]
        for i in range(2, n + 1):
            pair = 4 if s[i - 1] != s[i - 2] else 3
            cur = max(prev1 + 1, prev2 + pair)
            prev2, prev1 = prev1, cur
        return prev1