# You are given an integer mountainHeight denoting the height of a mountain.

# You are also given an integer array workerTimes representing the work time of workers in seconds.

# The workers work simultaneously to reduce the height of the mountain. For worker i:

# To decrease the mountain's height by x, it takes workerTimes[i] + workerTimes[i] * 2 + ... + workerTimes[i] * x seconds. For example:
# To reduce the height of the mountain by 1, it takes workerTimes[i] seconds.
# To reduce the height of the mountain by 2, it takes workerTimes[i] + workerTimes[i] * 2 seconds, and so on.
# Return an integer representing the minimum number of seconds required for the workers to make the height of the mountain 0.

 

# Example 1:

# Input: mountainHeight = 4, workerTimes = [2,1,1]

# Output: 3

# Explanation:

# One way the height of the mountain can be reduced to 0 is:

# Worker 0 reduces the height by 1, taking workerTimes[0] = 2 seconds.
# Worker 1 reduces the height by 2, taking workerTimes[1] + workerTimes[1] * 2 = 3 seconds.
# Worker 2 reduces the height by 1, taking workerTimes[2] = 1 second.
# Since they work simultaneously, the minimum time needed is max(2, 3, 1) = 3 seconds.


class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        

        #if mountain height can be reduced to 0 within t seconds
        #then it can also be reduced within any time greater than t seconds


        #we want to determine whetehr all workers together can reduce mountains height within mid seconds


        # can workers finish within 'seconds' ?
        def canFinish(seconds):

            totalReduced = 0

            for w in workerTimes:

                # max layers this worker can remove
                l, r = 0, mountainHeight

                while l <= r:
                    mid = (l + r) // 2

                    timeNeeded = w * (mid * (mid + 1)) // 2

                    if timeNeeded <= seconds:
                        l = mid + 1
                    else:
                        r = mid - 1

                totalReduced += r

                if totalReduced >= mountainHeight:
                    return True

            return False

        l = 0

        # worst case:
        # slowest worker does everything
        maxWorker = max(workerTimes)
        #for ith worker
        #the time to reduce montain by k units is
        #workertimes[i] x (1+2+...+k)

        # =workertimes[i] x k(k+1)/2
        r = maxWorker * (mountainHeight * (mountainHeight + 1)) // 2

        ans = r

        while l <= r:

            mid = (l + r) // 2

            if canFinish(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans