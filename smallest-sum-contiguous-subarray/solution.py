class Solution:
    def minSubarraySum(self, arr: list[int]) -> int:
        cur = best = arr[0]
        for x in arr[1:]:
            cur = min(x, cur + x)   # extend the current subarray or start a new one at x
            best = min(best, cur)
        return best