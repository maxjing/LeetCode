class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        index1 = len(S) - 1
        index2 = len(T) - 1
        while index1 >= 0 or index2 >= 0:
            i1 = self.findCharIndex(S, index1)
            i2 = self.findCharIndex(T, index2)
            if i1 < 0 and i2 < 0:
                return True
            if i1 < 0 or i2 < 0:
                return False
            if S[i1] != T[i2]:
                return False
            index1 = i1 - 1
            index2 = i2 - 1
        return True

    def findCharIndex(self, s, index):
        backSpace = 0
        while index >= 0:
            if s[index] == '#':
                backSpace += 1
            elif backSpace > 0:
                backSpace -= 1
            else:
                break
            index -= 1
        return index
