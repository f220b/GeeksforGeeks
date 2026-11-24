from collections import defaultdict

class Solution:
    def findPairs(self, arr: list[int]) -> list[int]:
        n = len(arr)
        groups = defaultdict(list)
        for i in range(n):
            ai = arr[i]
            for j in range(i + 1, n):
                groups[ai + arr[j]].append((i, j))

        best = None
        for g in groups.values():
            L = len(g)
            if L < 2:
                continue

            nxt = [L] * L
            for m in range(L - 2, -1, -1):
                nxt[m] = nxt[m + 1] if g[m + 1][0] == g[m][0] else m + 1

            for k in range(L):
                a, b = g[k]
                if best is not None and (a, b) > (best[0], best[1]):
                    break
                m = nxt[k]
                found = None
                while m < L:
                    c, d = g[m]
                    if c == b:
                        m = nxt[m]
                        continue
                    if d != b:
                        found = (c, d)
                        break
                    
                    if m + 1 < L and g[m + 1][0] == c:
                        found = g[m + 1]
                        break
                    m = nxt[m]
                if found:
                    cand = (a, b, found[0], found[1])
                    if best is None or cand < best:
                        best = cand
                    break

        return list(best) if best else [-1, -1, -1, -1]