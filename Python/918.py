class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        total, maxSum, currentMax, minSum, currentMin = 0, -math.inf, 0, math.inf, 0
        for n in A:
            currentMax = max(currentMax + n, n)
            maxSum = max(currentMax, maxSum)
            currentMin = min(currentMin + n, n)
            minSum = min(currentMin, minSum)
            total += n
        return max(maxSum, total - minSum) if maxSum > 0 else maxSum
    '''
    kadana algorithm
    1. get non-circular maximum as #53
    2. get circular min and min sum, use total - min sum subarray
    3. compare two maxsum
    '''
