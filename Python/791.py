class Solution:
    def customSortString(self, S: str, T: str) -> str:
        hash_map = collections.Counter(T)
        res = ""

        for char in S:
            if char in hash_map:
                res += char * hash_map[char]
                del hash_map[char]

        for key, value in hash_map.items():
            res += key * value

        return res