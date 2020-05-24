class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        columns = []
        res = []
        #get second matrix columns
        for i in range(len(B[0])):
            column = []
            for j in range(len(B)):
                column.append(B[j][i])
            columns.append(column)
        for i in range(len(A)):
            row = A[i]
            sublist = []
            for j in range(len(columns)):
                sublist.append(self.helper(row, columns[j]))
            res.append(sublist)
        return res

    def helper(self, l1, l2):
        sum = 0
        for i in range(len(l1)):
            sum += l1[i] * l2[i]
        return sum