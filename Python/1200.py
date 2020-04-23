# O(n) brute force
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minDiff = math.inf
        res = []
        for i in range(1, len(arr)):
            currentDiff = abs(arr[i] - arr[i - 1])
            if currentDiff > minDiff:
                continue
            else:
              # find smaller diff
                if currentDiff < minDiff:
                    minDiff = currentDiff
                    res.clear()
                res.append([arr[i - 1], arr[i]])
        return res
