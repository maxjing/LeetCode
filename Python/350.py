class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = Counter(nums1)
        d2 = Counter(nums2)
        res = []
        for k, v in d1.items():
            if k in d2:
                res.extend([k] * min(v, d2.get(k)))
        return res