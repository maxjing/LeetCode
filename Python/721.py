#dfs
class Solution(object):
    def accountsMerge(self, accounts):
        em_to_name = {}
        graph = collections.defaultdict(set)
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                graph[acc[1]].add(email)
                graph[email].add(acc[1])
                em_to_name[email] = name

        seen = set()
        ans = []
        for email in graph:
            if email not in seen:
                seen.add(email)
                stack = [email]
                component = []
                while stack:
                    node = stack.pop()
                    component.append(node)
                    for nei in graph[node]:
                        if nei not in seen:
                            seen.add(nei)
                            stack.append(nei)
                ans.append([em_to_name[email]] + sorted(component))
        return ans

'''
Time Complexity: O(∑ailog⁡ai)O(\sum a_i \log a_i)O(∑ai​logai​), where aia_iai​ is the length of accounts[i]. 
Without the log factor, this is the complexity to build the graph and search for each component. 
The log factor is for sorting each component at the end.
Space Complexity: O(∑ai)O(\sum a_i)O(∑ai​), the space used by our graph and our search.
'''

#union find
class Solution(object):
    def accountsMerge(self, accounts):
        parent = {}
        email_to_name = {}

        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            parent[find(i)] = find(j)

        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                email_to_name[email] = name
                union(email, account[1])  # account[1]: the first email

        trees = collections.defaultdict(list)
        for email in parent.keys():
            trees[find(email)].append(email)

        return [[email_to_name[root]] + sorted(emails) for (root, emails) in trees.items()]

