class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        #because we need combinataion not permutation so outerloop is coins
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[amount]
'''
https://www.youtube.com/watch?v=jaNZ83Q3QGc&feature=emb_logo
'''