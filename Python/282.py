class Solution:
    def addOperators(self, num, target):
        res, self.target = [], target
        for i in range(1, len(num) + 1):
            if i == 1 or (i > 1 and num[0] != "0"):  # prevent "00*" as a number
                self.dfs(num[i:], num[:i], int(num[:i]), int(num[:i]), res)  # this step put first number in the string
        return res

    def dfs(self, num, temp, cur, last, res):
        if not num:
            if cur == self.target:
                res.append(temp)
            return
        for i in range(1, len(num) + 1):
            val = num[:i]
            if i == 1 or (i > 1 and num[0] != "0"):  # prevent "00*" as a number
                self.dfs(num[i:], temp + "+" + val, cur + int(val), int(val), res)
                self.dfs(num[i:], temp + "-" + val, cur - int(val), -int(val), res)
                self.dfs(num[i:], temp + "*" + val, cur - last + last * int(val), last * int(val), res)


#my solution not work don't know why
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        self.target = target
        self.dfs(num, 0, "", res)
        return res

    def dfs(self, num, target, path, res):
        if len(num) == 0 and target == self.target:
            if path[0] == '+':
                path = path[1:]
            res.append(path)
        for i in range(len(num)):
            self.dfs(num[i + 1:], target + int(num[:i + 1]), path + "+" + num[:i + 1], res)
            self.dfs(num[i + 1:], target - int(num[:i + 1]), path + "-" + num[:i + 1], res)
            self.dfs(num[i + 1:], target * int(num[:i + 1]), path + "*" + num[:i + 1], res)
