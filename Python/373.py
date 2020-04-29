class Solution:
    def kSmallestPairs(self, nums1, nums2, k: int):
        maxHeap = []
        for i in range(min(k, len(nums1))):
            for j in range(min(k, len(nums2))):
                if len(maxHeap) < k:
                    heappush(maxHeap, (-nums1[i] - nums2[j], i, j))
                else:
                    if -nums1[i] - nums2[j] > maxHeap[0][0]:
                        heappop(maxHeap)
                        heappush(maxHeap, (-nums1[i] - nums2[j], i, j))
                    else:
                        break
        res = []
        while maxHeap:
            _, i, j = heappop(maxHeap)
            res.append([nums1[i], nums2[j]])
        return res


'''
Time: O(K​^2logK),
'''
