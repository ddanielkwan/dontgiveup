# Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

# Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

# After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

 

# Example 1:

# Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# Explanation:
# The first and second John's are the same person as they have the common email "johnsmith@mail.com".
# The third John and Mary are different people as none of their email addresses are used by other accounts.
# We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
# ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
       
        n = len(accounts)
        emails = [] #list of all emails seen
        #because some people can have same name, its better to use accid as the index and not name
        emailToIdx = {} #email -> emailidx
        emailToAccId = {} #emailidx to accid

        #step one populate everything
        idx = 0
        # Step 1: Give every unique email an ID
        for accId, account in enumerate(accounts):
            for i in range(1,len(account)):
                email = account[i]
                if email in emailToIdx:
                    continue
                emails.append(email)
                emailToIdx[email] = idx #this isemailindex
                emailToAccId[idx] = accId
                idx += 1

        # Step 2: Build graph connections
        adj = [[] for _ in range(idx)]
        for a in accounts:
            #connect all the emails
            #john, a, b
            #john, b , ca
            #a - b - c
            for i in range(2, len(a)):
                id1 = emailToIdx[a[i]]
                id2 = emailToIdx[a[i - 1]]
                adj[id1].append(id2)
                adj[id2].append(id1)
        
        emailGroup = defaultdict(list) # acc id -> list of emails, use for res
        visited = [False] * idx
        # Step 3: DFS every unvisited email node
        def dfs(node, accId):
            visited[node] = True
            emailGroup[accId].append(emails[node])
            for nei in adj[node]:
                if not visited[nei]:
                    dfs(nei, accId)
        # Step 4: Group emails by account/person
        for emailnode in range(idx):
            if not visited[emailnode]:
                dfs(emailnode, emailToAccId[emailnode])
        # Step 5: Sort emails and build final answer
        res = []
        for accId in emailGroup:
            name = accounts[accId][0]
            res.append([name] + sorted(emailGroup[accId]))
        
        return res
    
#n number of accounts
#k number of emails per account
# sorting all emails total which is n × k emails
#o(nxkx(nlogk))

#space onxk

