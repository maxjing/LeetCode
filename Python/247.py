class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        def helper(n):
            if n == 1:
                return ["0", "1", "8"]
            if n == 2:
                return ["00", "11", "69", "88", "96"]
            res = []
            for num in helper(n - 2):
                res += ["1" + num + "1", "6" + num + "9", "8" + num + "8", "9" + num + "6", "0" + num + "0"]
            return res
        #2020.05.28 the additional n == 1 check is for '0' in the helper '0' will be delete
        if n == 1:
            return helper(n)
        return [x for x in helper(n) if x[0] != '0']