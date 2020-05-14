class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        res = []
        i = 0
        j = 0
        while i < len(A) and j < len(B):
            #2020.05.14 use same 1. A[i][0] or 2. B[j][0] to compare with other one's 1 and 0
            a_overlap_b = A[i][0] >= B[j][0] and A[i][0] <= B[j][1]
            b_overlap_a = B[j][0] >= A[i][0] and B[j][0] <= A[i][1]

            if a_overlap_b or b_overlap_a:
                start = max(A[i][0], B[j][0])
                end = min(A[i][1], B[j][1])
                res.append([start, end])

            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        return res
