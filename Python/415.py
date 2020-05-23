class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        n = 1
        sum = 0
        while i >= 0 or j >= 0:
            a = num1[i] if i >= 0 else 0
            b = num2[j] if j >= 0 else 0
            currentSum = int(a) + int(b) + carry
            digit = currentSum % 10
            carry = currentSum // 10
            sum += digit * n
            n *= 10
            i -= 1
            j -= 1
        sum += carry * n
        return str(sum)

