class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        size = len(nums)
        nums.extend(nums)
        stack, res = [], [-1] * len(nums)
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                res[stack.pop()] = nums[i]
            stack.append(i)
        return res[:size]

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        size = len(nums)
        nums.extend(nums)
        res = []
        for i in range(len(nums)):
            if len(res) == size:
                break
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    res.append(nums[j])
                    break
            else:
                res.append(-1)
        return res