class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        res, carry = [], 0
        while i >= 0 or j >= 0:
            a = int(num1[i]) if i >= 0 else 0
            b = int(num2[j]) if j >= 0 else 0
            sum = a + b + carry
            digit = sum % 10
            carry = sum // 10
            res.append(digit)
            i -= 1
            j -= 1
        if carry != 0:
            res.append(carry)
        return ''.join([str(x) for x in res[::-1]])
