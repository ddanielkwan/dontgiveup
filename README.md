

Notes:
- is there a different way to think of question? What about flipping the question opposite?

Arrays

- Running Sum
- Prefix/Suffix
- swap
- keep track of the compliement inside a hashmapn

Two pointers


- how many pointers do we need?
- where do we start from? front or back?
- is it greedy? then do we need to sort? do we want most efficient matchups?
- can we use two pointers and math calculation?


Sliding Window
- always make sure window is valid first and then do compare for result 
- add latest element to window
- fix window
- measure window
- do we need to sort?
- be careful about where you place your measuring code, inside condition or after, be careful
- you can use queue as secondary DS


Stack
- stack for monodecreasing or monoincreasing
- we can store more than val, we can store (val, index, etc..)
- do we need specific order?
- must we always process when we see something
- if something breaks condtion must we pop?
- we can store max of already seen, or something we've alreay seen from previous 


Binary Search
- left pointer will always end at the first valid answer, because search space will always shrink

Linked List
- do we need dummy node to help us? sometimes we do
- its all about references don't forgot to think where the references are 
- we usually need an iterator 
- doubly linked list 


Trees
- dfs , bfs
- you can store more than 1 , 2 elements like 3 elemnts in bfs 
- dfs and bfs remember that you can add more parameters and it doesnt have to only be one 
- each level processing
- passing nodes 

Heap
- we can use min or max
- we can add more than one value
- priority
- double heaps
    
Graphs
- dfs, bfs
- you can cache reults
- topological sort
Intervals


Dynamic Programming 1D
- cache repitive work
- bottom up, e.g what is the longest subsequnce that ENDS AT THIS INDEX?
- number of ways

DP 2D
- tabulation(bottom up) although the loop is from top, at every stage you want to ask yourself, [r][c] where did i come from? what is the condtion from previous to now?

Ask yourself: "do I know the base case immediately?"
Base case is obvious/small → Bottom-up

You know dp[0][0] or dp[m-1][n-1] right away
You can fill the table in a natural order
Grid problems almost always bottom-up — start corner, fill to end corner

Subproblem structure is complex/sparse → Top-down (memoization)

Not every cell gets visited
The recursion tree is irregular — hard to know what order to fill
Example: word break, coin change with weird denominations

- what is the "state"
- number of ways
- can we space optimize withonly one row


Intervals
- sort intervals
- sweeping line, add start end to hashmap and count


Backtrack
- dfs start at index, keep state
-