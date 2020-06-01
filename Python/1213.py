class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        res = [x for x in arr1 if x in arr2 if x in arr3]
        return res