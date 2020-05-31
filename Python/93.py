class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        if len(s) > 12:
            return res
        self.dfs(s, res, 0, "", 0)
        return res

    def dfs(self, s, res, pos, digits, part):
        if part == 4 and pos == len(s):
            res.append(digits)
            return

        for i in range(1, 4):
            if pos + i > len(s):
                break
            sublist = s[pos:pos + i]
            # 2020.05.30 0,0,0,0 is fine so > 1 not > 0
            if len(sublist) > 1 and sublist[0] == '0' or int(sublist[:3]) >= 256:
                break
            self.dfs(s, res, pos + i, sublist if part == 0 else digits + '.' + sublist, part + 1)


class Solution:
    def restoreIpAddresses(self, s):
        res = []
        self.dfs(s, 0, "", res)
        return res

    def dfs(self, s, index, path, res):
        if index == 4:
            if not s:
                res.append(path[:-1])
            return  # backtracking
        for i in range(1, 4):
            # the digits we choose should no more than the length of s
            if i <= len(s):
                # choose one digit
                if i == 1:
                    self.dfs(s[i:], index + 1, path + s[:i] + ".", res)
                # choose two digits, the first one should not be "0"
                elif i == 2 and s[0] != "0":
                    self.dfs(s[i:], index + 1, path + s[:i] + ".", res)
                # choose three digits, the first one should not be "0", and should less than 256
                elif i == 3 and s[0] != "0" and int(s[:3]) <= 255:
                    self.dfs(s[i:], index + 1, path + s[:i] + ".", res)
