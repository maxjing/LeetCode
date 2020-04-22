class Solution:
    def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
        minCapitalHeap = []
        maxProfitHeap = []
        for i in range(len(Profits)):
            heappush(minCapitalHeap, (Capital[i], Profits[i]))
        availabelCapital = W
        for _ in range(k):
            while minCapitalHeap and minCapitalHeap[0][0] <= availabelCapital:
                capital, profit = heappop(minCapitalHeap)
                heappush(maxProfitHeap, (-profit))
            if not maxProfitHeap:
                break
            availabelCapital += -heappop(maxProfitHeap)
        return availabelCapital


'''
Time: O(nlogn)
'''
