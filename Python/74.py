class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1
        while l <= r:
            mid = l + (r - l) // 2
            num = matrix[mid//n][mid%n]
            if num == target:
                return True
            elif num < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
'''
mid // col -> row (carry)
mid % col -> column (digit)
'''


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #2020.05.20 remember to do empty check this for nested list
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        m, n = len(matrix), len(matrix[0]) - 1
        i, j = 0, 0
        rowToSearch = -1
        while i < m:
            currentMin = matrix[i][0]
            currentMax = matrix[i][n]
            if target in range(currentMin, currentMax + 1):
                rowToSearch = i
                break
            else:
                i += 1
        if rowToSearch == -1:
            return False
        else:
            return self.binarySearch(matrix[rowToSearch], target)

    def binarySearch(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False