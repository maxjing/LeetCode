class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        l, res = 0, 0
        d = {}
        for r in range(len(tree)):
            right = tree[r]
            d[right] = d.get(right, 0) + 1
            while len(d) > 2:
                left = tree[l]
                d[left] -= 1
                if d[left] == 0:
                    del d[left]
                l += 1
            res = max(res, r - l + 1)
        return res
