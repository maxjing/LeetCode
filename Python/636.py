class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        prev = 0
        for log in logs:
            fn, type, time = log.split(':')
            fn, time = int(fn), int(time)
            if type == 'start':
                if stack:
                    res[stack[-1]] += time - prev
                stack.append(fn)
                prev = time
            else:
                res[stack.pop()] += time - prev + 1
                prev = time + 1
        return res
