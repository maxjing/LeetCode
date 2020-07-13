class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        d = {}
        graph = defaultdict(set)
        for account in accounts:
            name = account[0]
            first_email = account[1]
            d[first_email] = name
            for email in account[1:]:
                graph[first_email].add(email)
                graph[email].add(first_email)

        seen, res = set(), []
        for email in d:
            q = deque([email])
            sublist = []
            name = d[email]
            while q:
                f_email = q.popleft()
                for node in graph[f_email]:
                    if node not in seen:
                        sublist.append(node)
                        seen.add(node)
                        q.append(node)
            if sublist:
                res.append([name] + sorted(sublist))
        return res


#bfs
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        d = {}
        graph = defaultdict(set)
        for account in accounts:
            name = account[0]
            first_email = account[1]
            d[first_email] = name
            for email in account[1:]:
                graph[first_email].add(email)
                graph[email].add(first_email)

        seen, res = set(), []
        for email in graph:
            if email not in seen:
                #start of new person
                name = d[email]
                q = deque([email])
                sublist = []
                while q:
                    f_email = q.popleft()
                    for node in graph[f_email]:
                        if node not in seen:
                            sublist.append(node)
                            seen.add(node)
                            q.append(node)
                res.append([name] + sorted(sublist))
        return res


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

