class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        maxLeft, maxRight = -math.inf, -math.inf
        l, r = 0, len(height) - 1
        while l <= r:
            if height[l] < height[r]:
                maxLeft = max(height[l], maxLeft)
                res += maxLeft - height[l]
                l += 1
            else:
                maxRight = max(height[r], maxRight)
                res += maxRight - height[r]
                r -= 1
        return res

'''
which side smaller, water goes there
'''