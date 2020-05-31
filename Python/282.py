class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        if not num or len(num) == 0:
            return res
        self.dfs(num, target, 0, '', 0, 0, res)
        return res

    def dfs(self, num, target, pos, path, cur, prev, res):
        if pos == len(num):
            if cur == target:
                res.append(path)
            return

        for i in range(pos, len(num)):
            sublist = num[pos: i + 1]
            # 2020.05.30  0x is not valid
            if len(sublist) > 1 and sublist[0] == '0':
                break
            n = int(sublist)
            if pos == 0:
                self.dfs(num, target, i + 1, str(n), n, n, res)
            else:
                self.dfs(num, target, i + 1, path + '+' + str(n), cur + n, n, res)
                self.dfs(num, target, i + 1, path + '-' + str(n), cur - n, -n, res)
                self.dfs(num, target, i + 1, path + '*' + str(n),
                         cur - prev + prev * n, prev * n, res)
 '''
 One easy way to calculate time complexity: There are n-1 slots for us to add an operator and there are 4 choices (+, -, * and no operator) so the complexity is 4^(N-1).
 '''
