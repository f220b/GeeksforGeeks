''' BST Node Structure
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def pairsViolatingBST(self, root):
        # 1. Iterative inorder traversal
        arr = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            arr.append(cur.data)
            cur = cur.right

        # 2. Count inversions using merge sort
        n = len(arr)
        temp = [0] * n

        def merge_count(lo, hi):
            if hi - lo <= 1:
                return 0
            mid = (lo + hi) // 2
            cnt = merge_count(lo, mid) + merge_count(mid, hi)
            i, j, k = lo, mid, lo
            while i < mid and j < hi:
                if arr[i] < arr[j]:
                    temp[k] = arr[i]; i += 1
                else:
                    temp[k] = arr[j]; j += 1
                    cnt += mid - i      # all remaining left elements > arr[j]
                k += 1
            while i < mid:
                temp[k] = arr[i]; i += 1; k += 1
            while j < hi:
                temp[k] = arr[j]; j += 1; k += 1
            arr[lo:hi] = temp[lo:hi]
            return cnt

        return merge_count(0, n)