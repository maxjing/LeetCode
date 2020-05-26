class Solution:
    def maximumSwap(self, num: int) -> int:
        if num <= 11:
            return num
        #digits = list(str(num))
        digits = [int(x) for x in str(num)]
        for i in range(len(digits) - 1):
            max_digit = max(digits[i + 1:])
            if digits[i] < max_digit:
                #here is to find the rightmost largest one
                max_digit_index = len(digits) - digits[::-1].index(max_digit) - 1
                digits[i], digits[max_digit_index] = digits[max_digit_index], digits[i]
                break
        # return int(''.join(map(str, digits)))
        return int(''.join([str(x) for x in digits]))

