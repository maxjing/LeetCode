class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0] * (num + 1)
        for i in range(1, num + 1):
            if i % 2 == 0:
                res[i] = res[i >> 1]
            else:
                res[i] = res[i - 1] + 1
        return res


'''
奇数 以1结尾
偶数 以0结尾
奇数时 bit 1 等于前面哪个数 + 1
偶数时 等于 无视 这个数 >> 1
If it is even, the ending bit is 0, then that bit can be ignored, 
countBits(num) is the same as countBits(num >> 1), so countBits(num) = countBits(num >> 1);

For example:

num:      101010101010
num >> 1: 10101010101

If it is odd, the ending bit is 1, then the number of set bits is that of num - 1 + 1, 
i.e. countBits(num) = countBits(num - 1) + 1

For example:

num:     101010101011
num - 1: 101010101010
        '''
