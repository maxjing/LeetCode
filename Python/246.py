class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        d = {}
        d['8'] = '8'
        d['9'] = '6'
        d['6'] = '9'
        d['1'] = '1'
        d['0'] = '0'

        l, r = 0, len(num) - 1
        while l <= r:
            left, right = num[l], num[r]
            if left not in d or right not in d:
                return False
            elif d[left] != right:
                return False
            l += 1
            r -= 1
        return True