def minRemoveToMakeValid(self, s):
    bad = set()
    stack = []
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        elif c == ')':
            if stack:
                stack.pop()
            else:
                bad.add(i)
    #2020.05.24 |= 用于set的话 就是两个加起来
    bad |= set(stack)
    return ''.join(c for i, c in enumerate(s) if i not in bad)