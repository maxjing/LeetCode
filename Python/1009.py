class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        bit_count, n = 0, N
        while n > 0:
            bit_count += 1
            n = n >> 1
      # 2^2 = 4 4- 1 = 3 -> 11
      # 2^3 = 8 8-7 = 7 -> 111
        all_ones = pow(2, bit_count) - 1
        return N ^ all_ones
