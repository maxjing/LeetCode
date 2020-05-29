class Solution:
    def simplifyPath(self, path):
        stack = []
        for token in path.split('/'):
        #2020.05.28 notice, '' will in the splited array
        #e.g ' a b'.split(' ') -> '', a, b
            if token in ('', '.'):
                continue
            elif token == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(token)
        return '/' + '/'.join(stack)
