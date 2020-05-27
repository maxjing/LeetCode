class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        ascending = True
        descending = True

        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                ascending = False
            if A[i] < A[i + 1]:
                descending = False

        return ascending or descending
