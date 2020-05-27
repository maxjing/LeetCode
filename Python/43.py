class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(self.strToInt(num1) * self.strToInt(num2))

    def strToInt(self, s):
        res = 0
        prod = 1
        for i in range(len(s) - 1, -1, -1):
            res += int(s[i]) * prod
            prod *= 10
        return res
