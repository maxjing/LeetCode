class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum, res, d = 0, 0, {}
        d[0] = 1
        for i in range(len(nums)):
            sum += nums[i]
            res += d.get(sum - k, 0)
            d[sum] = d.get(sum, 0) + 1
        return res

'''
sum[i, j] = sum[0, j] - sum[0, i - 1]    --> sum[0, i - 1] = sum[0, j] - sum[i, j]
    k           sum      hashmap-key     -->  hashmap-key  =  sum - k

https://leetcode.com/problems/subarray-sum-equals-k/discuss/190674/Python-O(n)-Based-on-%22running_sum%22-concept-of-%22Cracking-the-coding-interview%22-book
[1, 2, 1, 3], k = 3 -> [1, 3, 4, 7] 
{[0, 3], [1, 4], [7,4]} diff 3
#prefix_sum = sum - k equals subarray equals k
https://leetcode.com/problems/subarray-sum-equals-k/discuss/341399/Python-clear-explanation-with-code-and-example
'''

