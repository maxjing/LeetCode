class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        window_start, max_len, max_ones = 0, 0, 0
        for window_end in range(len(A)):
            if A[window_end] == 1:
                max_ones += 1

            while(window_end - window_start + 1 - max_ones > K):
                if(A[window_start] == 1):
                    max_ones -= 1
                window_start += 1
            max_len = max(max_len, window_end - window_start + 1)

        return max_len
