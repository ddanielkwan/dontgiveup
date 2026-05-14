# You are given an integer array nums of length n.

# You start at index 0, and your goal is to reach index n - 1.

# From any index i, you may perform one of the following operations:

# Adjacent Step: Jump to index i + 1 or i - 1, if the index is within bounds.
# Prime Teleportation: If nums[i] is a prime number p, you may instantly jump to any index j != i such that nums[j] % p == 0.
# Return the minimum number of jumps required to reach index n - 1.

 

# Example 1:

# Input: nums = [1,2,4,6]

# Output: 2

# Explanation:

# One optimal sequence of jumps is:

# Start at index i = 0. Take an adjacent step to index 1.
# At index i = 1, nums[1] = 2 is a prime number. Therefore, we teleport to index i = 3 as nums[3] = 6 is divisible by 2.
# Thus, the answer is 2.

# Example 2:

# Input: nums = [2,3,4,7,9]

# Output: 2

# Explanation:

# One optimal sequence of jumps is:

# Start at index i = 0. Take an adjacent step to index i = 1.
# At index i = 1, nums[1] = 3 is a prime number. Therefore, we teleport to index i = 4 since nums[4] = 9 is divisible by 3.
# Thus, the answer is 2.

class Solution:
    def minJumps(self, nums):
        n = len(nums)
        # prime it is divisible only by 1 and itself
        # check prime Try dividing by every number from 2 to n-1.
        def is_prime(x):
            if x < 2:
                return False

            for d in range(2, x):
                if x % d == 0:
                    return False

            return True

        # prime -> indices divisible by prime
        divisible = defaultdict(list)

        primes = set(num for num in nums if is_prime(num))
        #just geting index
        for p in primes:
            for i, val in enumerate(nums):
                if val % p == 0:
                    divisible[p].append(i)

        q = deque([(0, 0)])  # (index, distance)
        visited = set([0])

        used_prime = set()

        while q:
            i, dist = q.popleft()

            if i == n - 1:
                return dist

            # adjacent moves
            for ni in [i - 1, i + 1]:
                if 0 <= ni < n and ni not in visited:
                    visited.add(ni)
                    q.append((ni, dist + 1))

            # teleport
            val = nums[i]

            if is_prime(val) and val not in used_prime:
                for ni in divisible[val]:

                    if ni not in visited:
                        visited.add(ni)
                        q.append((ni, dist + 1))

                used_prime.add(val)