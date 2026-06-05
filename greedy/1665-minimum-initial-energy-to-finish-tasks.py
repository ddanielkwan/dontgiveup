# You are given an array tasks where tasks[i] = [actuali, minimumi]:

# actuali is the actual amount of energy you spend to finish the ith task.
# minimumi is the minimum amount of energy you require to begin the ith task.
# For example, if the task is [10, 12] and your current energy is 11, you cannot start this task.
#  However, if your current energy is 13, you can complete this task, and your energy will be 3 after finishing it.

# You can finish the tasks in any order you like.

# Return the minimum initial amount of energy you will need to finish all the tasks.

 

# Example 1:

# Input: tasks = [[1,2],[2,4],[4,8]]
# Output: 8
# Explanation:
# Starting with 8 energy, we finish the tasks in the following order:
#     - 3rd task. Now energy = 8 - 4 = 4.
#     - 2nd task. Now energy = 4 - 2 = 2.
#     - 1st task. Now energy = 2 - 1 = 1.
# Notice that even though we have leftover energy, starting with 7 energy does not work because we cannot do the 3rd task.

class Solution1:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        #binary search
        # tasks with bigger (minimum - actual)
        # should be done earlier
        tasks.sort(key=lambda t: (t[1] - t[0]), reverse=True)

        def canFinish(energy):

            cur = energy

            for actual, minimum in tasks:

                # cannot even start this task
                if cur < minimum:
                    return False

                # spend energy
                cur -= actual

            return True

        # binary search answer
        left = 0
        right = sum(b for a, b in tasks) 

        while left < right:

            mid = (left + right) // 2

            if canFinish(mid):
                right = mid
            else:
                left = mid + 1

        return left



#greedy

class Solution:
    # "How much energy must I have BEFORE this task?"
    def minimumEffort(self, tasks: List[List[int]]) -> int:
            #[1,100] barely need real energy but need a lot of start
            #so we borrow from smaller ones

        tasks.sort(key=lambda t: (t[1] - t[0]))
     
        energy = 0
      

        #that would mean we need either 20+5, or minimum to get it done
        # so thats why its max
        for actual, minimum in tasks:

            energy = max(energy + actual, minimum)

        return energy

#doing the tasks backwards