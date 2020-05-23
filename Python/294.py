def canWin(self, s):
    for i in range(len(s)-1):
        if s[i] == '+' and s[i+1] == '+' and not self.canWin(s[:i]+'--'+s[i+2:]):
            return True
    return False

#with memorization
class Solution(object):
    def canWin(self, s):
        self.memo = {}
        return self.can(s)

    def can(self, s):
        if s in self.memo:
            return self.memo[s]
        for i in range(len(s) - 1):
            if s[i] == '+' and s[i + 1] == '+' and not self.can(s[:i] + '--' + s[i + 2:]):
                self.memo[s] = True
                return True
        self.memo[s] = False
        return False


