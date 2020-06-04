class Solution:
    def reverseVowels(self, s: str) -> str:
        s_arr = [c for c in s]
        l, r = 0, len(s_arr) - 1
        while l < r:
            if s_arr[l] in 'aeiouAEIOU' and s_arr[r] in 'aeiouAEIOU':
                s_arr[l], s_arr[r] = s_arr[r], s_arr[l]
                l += 1
                r -= 1
            if s_arr[l] not in 'aeiouAEIOU':
                l += 1
            if s_arr[r] not in 'aeiouAEIOU':
                r -= 1
        return ''.join(s_arr)