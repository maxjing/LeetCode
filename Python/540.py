# O(logn)
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if mid % 2 == 1:
              # reach the left one of the middle pair
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                # search right
                lo = mid + 2
            else:
                # search left
                hi = mid - 1
        return nums[lo]


# O(n) brute force
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        d = {}
        for n in nums:
            if n not in d:
                d[n] = 0
            d[n] += 1

        for key, value in d.items():
            if value == 1:
                return key

        return None
