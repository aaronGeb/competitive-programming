# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        
        def find(x):
            parent.setdefault(x, x)
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent[find(x)] = find(y)
        
        email_to_name = {}
        
        # 1. Union emails within each account
        for acc in accounts:
            name = acc[0]
            first_email = acc[1]
            for email in acc[1:]:
                union(first_email, email)
                email_to_name[email] = name
        
        # 2. Group by root
        groups = defaultdict(list)
        for email in email_to_name:
            root = find(email)
            groups[root].append(email)
        
        # 3. Build result
        result = []
        for root, emails in groups.items():
            result.append([email_to_name[root]] + sorted(emails))
        return result
