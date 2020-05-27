class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n < 0:
            return 1/self.myPow(x,-n)
        if n%2 == 0:
            #2 ^ 4 -> 2^2^2
            return self.myPow(x*x,n/2)
        else:
            #2^3 -> 2 * 2^2
            return x*self.myPow(x,n-1)

