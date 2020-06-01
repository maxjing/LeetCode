class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        num, den = numerator, denominator
        if den == 0:
            return
        if num == 0:
            return '0'
        res = []
        if (num < 0) ^ (den < 0):
            res.append('-')
        num, den = abs(num), abs(den)
        res.append(str(num // den))
        rmd = num % den
        if rmd == 0:
            return "".join(res)
        res.append('.')
        d = {}
        while rmd:
            if rmd in d:
                res.insert(d[rmd], "(")
                res.append(')')
                break
            d[rmd] = len(res)
            div, rmd = divmod(rmd * 10, den)
            res.append(str(div))
        return "".join(res)
