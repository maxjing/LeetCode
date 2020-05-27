class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for s in strings:
            key = []
            for i in range(len(s) - 1):
                diff = ord(s[i + 1]) - ord(s[i])
                #or diff = 26 + ord(s[i + 1] - ord(s[i])
                #key.append(diff % 26)
                real_diff = diff if diff > 0 else diff + 26
                key.append(real_diff)
            d[tuple(key)].append(s)
        return d.values()