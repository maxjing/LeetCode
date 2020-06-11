class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack, d = [], defaultdict(dict)
        for n in nums2:
            while stack and stack[-1] < n:
                d[stack.pop()] = n
            stack.append(n)

        res = []
        for n in nums1:
            res.append(d.get(n, -1))
        return res


'''
[9, 8, 7, 3, 2, 1, 6] 遇到6的时候 3, 2, 1都会被pop, 他们都ngn 就是6
'''


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for n in nums1:
            pos = nums2.index(n)
            if pos == len(nums2) - 1:
                res.append(-1)
            else:
                for i in range(pos + 1, len(nums2)):
                    if nums2[i] > n:
                        res.append(nums2[i])
                        break
                else:
                    res.append(-1)
        return res
