class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        total = 0
        for i in range(n):
            freq = [0] * 26
            for j in range(i, n):
                freq[ord(s[j]) - 97] += 1
                mx, mn = 0, n + 1
                for f in freq:
                    if f:
                        if f > mx: mx = f
                        if f < mn: mn = f
                total += mx - mn
        return total