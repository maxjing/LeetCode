class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = -math.inf
        while l <= r:
            a = min(height[l], height[r]) * (r - l)
            res = max(a, res)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res
