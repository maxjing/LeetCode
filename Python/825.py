class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        c = Counter(ages)
        res = 0
        for k1, v1 in c.items():
            for k2, v2 in c.items():
                if not k2 <= k1 / 2 + 7 and not k2 > k1:
                    res += v1 * v2
            #remove self request self 
                    if k1 == k2:
                        res -= v1
        return res