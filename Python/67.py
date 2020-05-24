class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        res = []
        while i >= 0 or j >= 0:
            s1 = int(a[i]) if i >= 0 else 0
            s2 = int(b[j]) if j >= 0 else 0
            digit = (s1 + s2 + carry) % 2
            carry = (s1 + s2 + carry) // 2
            res.append(digit)
            i -= 1
            j -= 1
        if carry != 0:
            res.append(carry)
        res.reverse()
        return "".join(str(x) for x in res)
