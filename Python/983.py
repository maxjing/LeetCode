class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        arr = [0] * 366
        for d in days:
            arr[d] = 1
        dp = [0]
        for i in range(1, len(arr)):
            if arr[i] == 0:
                dp.append(dp[-1])
            else:
                tmp = dp[-1] + costs[0]
                tmp = min(tmp, costs[1]+ (dp[-7] if i-7>=0 else 0) )
                tmp = min(tmp, costs[2]+ (dp[-30] if i-30>=0 else 0) )
                dp.append(tmp)
        return dp[-1]