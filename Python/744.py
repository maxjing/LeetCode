class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        if target > letters[n - 1] or target < letters[0]:
            return letters[0]
        l, r = 0, n - 1
        while l <= r:
            mid = l + (r - l) // 2
            if target < letters[mid]:
                r = mid - 1
            # including target == letters[mid]
            else:
                l = mid + 1
        return letters[l % n]


'''
cannot below, cause when target == letters[mid], we want pointer to move forward
if target > letters[mid]:
    l = mid + 1
else:
    r = mid - 1

'''
