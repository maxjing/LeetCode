class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = Counter(s)
        d2 = Counter(t)
        if len(d1) != len(d2):
            return False
        for k, v in d1.items():
            if d1[k] != d2[k]:
                return False
        return True
