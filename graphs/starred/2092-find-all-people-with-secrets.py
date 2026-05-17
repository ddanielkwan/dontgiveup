# You are given an integer n indicating there are n people numbered from 0 to n - 1. You are also given a 0-indexed 2D integer array meetings where meetings[i] = [xi, yi, timei] indicates that person xi and person yi have a meeting at timei. A person may attend multiple meetings at the same time. Finally, you are given an integer firstPerson.

# Person 0 has a secret and initially shares the secret with a person firstPerson at time 0. This secret is then shared every time a meeting takes place with a person that has the secret. More formally, for every meeting, if a person xi has the secret at timei, then they will share the secret with person yi, and vice versa.

# The secrets are shared instantaneously. That is, a person may receive the secret and share it with people in other meetings within the same time frame.

# Return a list of all the people that have the secret after all the meetings have taken place. You may return the answer in any order.

 

# Example 1:

# Input: n = 6, meetings = [[1,2,5],[2,3,8],[1,5,10]], firstPerson = 1
# Output: [0,1,2,3,5]
# Explanation:
# At time 0, person 0 shares the secret with person 1.
# At time 5, person 1 shares the secret with person 2.
# At time 8, person 2 shares the secret with person 3.
# At time 10, person 1 shares the secret with person 5.​​​​
# Thus, people 0, 1, 2, 3, and 5 know the secret after all the meetings.

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:

        #intuiton: Meetings at the SAME time form a temporary graph
        #n people
        #2d array meetings, [x,y, time] person x and person y have meeting during time
        #person can attend multiple meetings at same time, how

        #first person,
        #person 0 has secret and init shares with firstperson at time 0
        #seceret shared every time meeting takes place with person that has the secret

        #observation, instanteously
        
        #[2,3,5] #does not know secret rihtn ow
        #[3,4,5] #same
        #[1,2,5] #suddenly two knowds so 2->3->4 knows intantly

        secrets = set([0, firstPerson]) #people with secrest

        #split meetings based on time

        #time map
        time_map = {} #time -> to adj list of meetigns that occur at that time
        
        for src, dst, time in meetings:
            if time not in time_map:
                time_map[time] = defaultdict(list)
            time_map[time][src].append(dst)
            time_map[time][dst].append(src)
        def dfs(src, adj):
            if src in visit:
                return
            
            visit.add(src)
            secrets.add(src)
            for nei in adj[src]:
                dfs(nei, adj)
            
        for t in sorted(time_map.keys()): #all unique times
            visit = set()
            for src_node in time_map[t]: #in this adj list, we have every edge in that adj list, we want to consieder every single key in this adj list and consdier as src node, we want to contemplate shold we run a dfs or not from this src, we onyl run if the src is in secrets because only then can secret be spread to other nodes
                if src_node in secrets:
                    dfs(src_node, time_map[t])

        return list(secrets)

# O(M log M)