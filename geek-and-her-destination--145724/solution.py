class Solution:
    def minTime(self, a: int, b: int, d: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        c = a - b

        def S(n):
            m = n - a
            if m <= 0:
                return 0
            q, rem = divmod(m, c)
            return c * q * (q + 1) // 2 + rem * (q + 1)

        L, R = d - r, d - l
        cnt = R - L + 1
        base = (L + R) * cnt // 2 + cnt
        extra = 2 * b * (S(R) - S(L - 1))
        return (base + extra) % MOD
