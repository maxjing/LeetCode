class Solution:
    def toGoatLatin(self, S):
        out = []
        for i, w in enumerate(S.split(' ')):
            if w[0] not in list('aeiouAEIOU'):
                w = w[1:] + w[0]
            out.append(w + 'ma' + 'a'*(i+1))
        return ' '.join(out)

class Solution:
    def toGoatLatin(self, S: str) -> str:
        s = S.split(' ')
        v = ['a', 'e', 'i', 'o','u']
        v1 = ['A', 'E', 'I','O', 'U']
        res = []
        for i in range(len(s)):
            a = ['a'] * (i + 1)
            sublist = []
            if s[i][0] in v or s[i][0] in v1:
                sublist.append(s[i])
                sublist.append('ma')
                sublist.extend(a)
            else:
                sublist.append(s[i][1:])
                sublist.append(s[i][0])
                sublist.append('ma')
                sublist.extend(a)
            res.append("".join(sublist))
        return " ".join(res)