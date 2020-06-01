class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjacency = defaultdict(list)
        tickets.sort(reverse=True)
        for src, dest in tickets:
            adjacency[src].append(dest)

        res = []
        stack = ["JFK"]
        while stack:
            src = stack[-1]
            if adjacency[src]:
                stack.append(adjacency[src].pop())
            else:
                res.append(stack.pop())
        return res[::-1]
