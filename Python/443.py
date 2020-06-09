class Solution:
    def compress(self, chars: List[str]) -> int:
        i, j = 0, 0
        while i < len(chars):
            curr = chars[i]
            count = 0
            while i < len(chars) and chars[i] == curr:
                i += 1
                count += 1
            chars[j] = curr
            j += 1
            if count > 1:
                for c in str(count):
                    chars[j] = c
                    j += 1
        return j