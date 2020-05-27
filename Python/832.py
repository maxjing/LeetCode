class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        res = []
        for l in A:
            l.reverse()
            sublist = []
            for n in l:
                #1->0 0->1
                sublist.append(n ^ 1)
            res.append(sublist)

        return res
