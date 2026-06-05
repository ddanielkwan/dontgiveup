

Notes:
- is there a different way to think of question? What about flipping the question opposite?

Arrays

- Running Sum
- Prefix/Suffix
- keep tracking of prefix from up and left

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
- you dont need to only move left, you can also fix left and move rih
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
- soemetimes abotu finding trnasition point monotonic
- find position that holds true etc

Linked List
- do we need dummy node to help us? sometimes we do
- its all about references don't forgot to think where the references are 
- we usually need an iterator 
- doubly linked list 


Trees
- dfs , bfs
- dfs for iterative for post order you need visited set
- you can store more than 1 , 2 elements like 3 elemnts in bfs 
- dfs and bfs remember that you can add more parameters and it doesnt have to only be one 
- each level processing
- passing nodes 

Heap
- we can use min or max
- ineed reepeated access to smalllest or largest or bet availbel
- we can add more than one value
- priority, we usualyl use in parallel with queeues
- double heaps
    
Graphs
- dfs, bfs
- for bfs, it doesnt have to be node, it can be state e.g like boardgame, like string from 000 to 001, like locks, anytin can be. node
- you can cache reults
- topological sort
Intervals
- for intervals a lot of times you compare with prev
- also some are greedy
- w can also use a tree to compare intervals
- we can use the hashmap to store when starts ends e.g [1,5] -> hashmap hashmap[1] = 1 hashmap[6] = -1


Dynamic Programming 1D
- cache repitive work
- bottom up, e.g what is the longest subsequnce that ENDS AT THIS INDEX?
- number of ways

DP 2D
- tabulation(bottom up) although the loop is from top, at every stage you want to ask yourself, [r][c] where did i come from? what is the condtion from previous to now?
- were alwys jjust populatin something
- sometimes if its asking for 1 v 1 like alice vs bob or robot 1 vs robot 2,
you canthink of making dfs for one person optimally 

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



2d matrix math
- precompute adding sides or top




We can ask: what invariants (conditions that remain true after making any move) there are. This is natural for any question that involves transforming some state and asking whether a final state is possible.

Advanced Graphs
- Djisktras - uses min heap for (pathcost and node)
- Prims - uses min heap calculates min cost to connect all nodes


can i think backwards?

How can i rearrange the input or preprocess it differently
If i can solve it mentally then i know the algorithm,just think
we can modify an alogitthm to fit the data astructure
or modify the data structure to fit the algorithm


## Things to Remember by Topic

### Arrays
- Use a hashmap when you need fast lookup.
- Use prefix sums when a range or subarray sum is involved.
- Sort when order does not matter and comparisons become easier.
- Think about whether you need one pass, two passes, or extra space.

### Strings
- Count characters when comparing frequency.
- Use two pointers for matching from both ends.
- Use a hashmap/window for substring problems.
- Be careful with indexes and off-by-one errors.

### Two Pointers
- Usually works on sorted arrays, strings, or linked lists.
- Decide where pointers start: both ends, same side, or fast/slow.
- Move the pointer that helps fix the current problem.
- Sorting often makes two pointers possible.

### Sliding Window
- Expand the right side to include more.
- Shrink the left side when the window becomes invalid.
- Update the answer only when the window is valid.
- Track only what the window needs: count, sum, max, frequency, etc.

### Stack
- Use a stack when the most recent item matters first.
- Use a monotonic stack for next greater/smaller problems.
- Store indexes when distance or position matters.
- Pop when the current value resolves previous values.

### Binary Search
- Use when the data is sorted or the answer space is searchable.
- Ask: "Is this middle value valid?"
- If valid, try to find a better answer.
- Be clear whether you are finding first valid or last valid.

### Linked List
- Use a dummy node to simplify head changes.
- Save `next` before changing pointers.
- Fast and slow pointers help find middle, cycles, or nth from end.
- Think carefully about references, not just values.

### Trees
- DFS is good for subtree information.
- BFS is good for level-by-level problems.
- Recursion should return what the parent needs.
- Add extra parameters when the path or depth matters.

### Graphs
- Build adjacency lists when nodes connect to other nodes.
- Use BFS for shortest path in unweighted graphs.
- Use DFS for exploring components or islands.
- Use topological sort when there are dependencies.

### Advanced Graphs
- Dijkstra uses a min heap for shortest paths with positive weights.
- Prim uses a min heap to connect all nodes with minimum cost.
- Union Find helps with connected components and cycles.
- Always know what each edge weight means.

### Heap
- Use a heap when you repeatedly need smallest or largest.
- Python has a min heap by default.
- For max heap, push negative values.
- Store tuples like `(priority, value)` when needed.

### Intervals
- Sort intervals first.
- Merge when intervals overlap.
- Greedy usually works by sorting by start or end.
- Sweep line works when many starts and ends affect a count.

### Dynamic Programming 1D
- Define what `dp[i]` means before coding.
- Think: "What smaller answer helps build this one?"
- Set base cases clearly.
- Common patterns: max/min result, number of ways, true/false possible.

### Dynamic Programming 2D
- Define what `dp[r][c]` or `dp[i][j]` means.
- Ask where the current cell/state can come from.
- Grid DP usually builds from a corner.
- Space optimize only after the full table idea is clear.

### Backtracking
- Build the answer one choice at a time.
- Use `start` index when order should not repeat.
- Undo choices before trying the next branch.
- Prune early when a partial answer cannot work.

### Greedy
- Sort if it helps make the best local choice.
- Prove the local choice does not hurt future choices.
- Greedy often tracks one best current value.
- If greedy is hard to prove, DP may be needed.

### Trie
- Use a trie for prefix problems.
- Each node represents a character path.
- Mark the end of a word.
- Good for autocomplete, word search, and prefix lookup.

### Math
- Look for a formula or invariant.
- Avoid simulating if counting is enough.
- Think about parity, modulo, distance, and bounds.
- Work through small examples to see the pattern.


## Tricks to Remember

### BFS Tricks
- A BFS node does not have to be one item from the input.
- Sometimes the node should be a state, route, word, mask, position, or level.
- For Bus Routes, think of each bus route as a node, not each bus stop.
- BFS layers usually mean number of moves, jumps, buses, swaps, or transformations.
- If the problem asks for minimum steps in an unweighted graph, think BFS.
- Track visited states, not just visited values.

### Graph Modeling Tricks
- First ask: "What should be a node?"
- Then ask: "When are two nodes connected?"
- A grid cell can be a node.
- A word can be a node.
- A route can be a node.
- A bitmask can be a node.
- A position plus extra info can be a node, like `(row, col, keys)`.

### Reverse Thinking
- Try starting from the target instead of the source.
- Multi-source BFS works when many starting points spread at the same time.
- For Pacific Atlantic Water Flow, start from the oceans and move backward.
- For rotting oranges, start from all rotten oranges at once.

### State Tricks
- If one value is not enough, add more to the state.
- State can include index, count, previous value, remaining moves, or mode.
- In BFS/DFS, visited may need to store the full state, not just the node.
- Example: `(node, stops)` is different from just `node`.

### Sorting Tricks
- Sort when pairing, grouping, merging, or greedily choosing.
- Sorting can turn a hard comparison into an adjacent comparison.
- After sorting, two pointers or greedy often becomes possible.

### Hashmap Tricks
- Store what you need later, not just what you have now.
- For Two Sum, store numbers already seen so you can find the complement.
- For prefix sums, store previous sums to find a target range quickly.
- Frequency maps help compare strings, windows, and groups.

### DP Tricks
- Ask: "What does this state mean?"
- Ask: "What smaller state did this come from?"
- For subsequence DP, think about answers that end at index `i`.
- For grid DP, think about where the current cell came from.
- For choice DP, think take or skip.

### Monotonic Stack Tricks
- Use when each item needs the next greater or next smaller value.
- The stack stores unresolved items.
- Current value may resolve many previous values.
- Store indexes if you need distance or width.

### Union Find Tricks
- Use when the problem keeps asking what belongs together.
- Good for components, cycles, and merging groups.
- If connecting two nodes creates a cycle, Union Find can detect it.
