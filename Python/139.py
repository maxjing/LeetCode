class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False] * len(s)
        for i in range(1, len(s) + 1):
            for word in wordDict:
                if s[:i].endswith(word):
                    dp[i] |= dp[i-len(word)]
        return dp[-1]