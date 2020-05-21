class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = deque()
        res.append((digits[-1] + 1) % 10)
        carry = (digits[-1] + 1) // 10
        for i in range(len(digits) - 2, -1, -1):
            sum = digits[i] + carry
            digit = sum % 10
            carry = sum // 10
            res.appendleft(digit)
        if carry == 0:
            return res
        else:
            res.appendleft(carry)
            return res

'''
digit % 10
carry // 10
'''