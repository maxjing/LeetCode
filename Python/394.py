class Solution:
    def decodeString(self, s: str) -> str:
        curr_string, curr_num, stack = '', 0, []
        for c in s:
            if c.isdigit():
                curr_num = curr_num * 10 + int(c)
            elif c.isalpha():
                curr_string += c
            elif c == '[':
                stack.append(curr_string)
                stack.append(curr_num)
                curr_string = ''
                curr_num = 0
            elif c == ']':
                num = stack.pop()
                prev_string = stack.pop()
                curr_string = prev_string + curr_string * num
        return curr_string