class Solution:
    def largestNumber(self, nums):
        for i in range(len(nums), 0, -1):
            for j in range(i - 1):
                if not self.compare(nums[j], nums[j + 1]):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return str(int("".join(map(str, nums))))

    def compare(self, n1, n2):
        return str(n1) + str(n2) > str(n2) + str(n1)

'''
str(int(str()))  because [0,0] will give 00 so change to int then str again
'''

class LargerNumKey(str):
    def __lt__(x, y):
        return x + y < y + x


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        a = []

        for num in nums:
            a.append(str(num))
        a.sort(reverse=True, key=LargerNumKey)

        if a[0] == '0':
            return '0'
        return ''.join(a)



