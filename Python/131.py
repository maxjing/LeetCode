class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.helper(s, 0, [], res)
        return res

    def helper(self, s, start, part, res):
        if start == len(s):
            res.append(part)
        for i in range(start, len(s)):
            sub = s[start:i+1]
            if self.isPalindrome(sub):
                self.helper(s, i+1, part + [sub], res)

    def isPalindrome(self, s):
        return s == s[::-1]
