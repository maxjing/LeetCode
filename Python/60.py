class Solution:
    def getPermutation(self, n, k):
        res, nums = "", [x for x in range(1, n + 1)]
        k -= 1
        while n:
            n -= 1
            index, k = divmod(k, factorial(n))
            res += str(nums.pop(index))
        return res


'''
for n there are factorial(n)
say n = 4, you have {1, 2, 3, 4}
If you were to list out all the permutations you have
1 + (permutations of 2, 3, 4)

2 + (permutations of 1, 3, 4)

3 + (permutations of 1, 2, 4)

4 + (permutations of 1, 2, 3)

14th one 13/6(3!) = 2 -> first digit 3
'''
