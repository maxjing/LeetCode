class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1, d2 = {}, {}
        for i, val in enumerate(s):
            d1[val] = d1.get(val, []) + [i]
        for i, val in enumerate(t):
            d2[val] = d2.get(val, []) + [i]
        return sorted(d1.values()) == sorted(d2.values())
'''
only need to record the index and sorted
'''

#2020.05.22 by myself
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d1, d2 = {}, {}
        l1, l2 = [], []
        for i in range(len(s)):
            if s[i] not in d1:
                d1[s[i]] = [s[i], i]
            l1.append(d1[s[i]][1])
        for i in range(len(t)):
            if t[i] not in d2:
                d2[t[i]] = [t[i], i]
            l2.append(d2[t[i]][1])
        for i in range(len(l1)):
            if l1[i] != l2[i]:
                return False
        return True
