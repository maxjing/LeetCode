class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        tickets.sort(reverse=True)
        for u, v in tickets:
            graph[u].append(v)

        stack = ["JFK"]
        res = []
        while stack:
            u = stack[-1]
            if graph[u]:
                stack.append(graph[u].pop())
            else:
                res.append(stack.pop())
        return res[::-1]


'''
remember to sort reverse first, so the greater lexi order will be popped first
until cannot go anywhere else, means used up all its destination, means this one should be last stop, add it to result
'''