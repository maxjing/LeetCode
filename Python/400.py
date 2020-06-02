class Solution(object):
    def findNthDigit(self, n):
        start, size, step = 1, 1, 9
        while n > size * step:
            n -= size * step
            size += 1
            step *= 10
            start *= 10
        digit_string = str(start + (n - 1) // size)
        return digit_string[(n - 1) % size]
