# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?

 

# Example 1:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # We want the k-th LARGEST number.
        # But quickselect naturally finds the k-th SMALLEST position.
        #
        # Example:
        # nums sorted ascending: [1,2,3,4,5,6]
        # 2nd largest = 5
        # Index of 5 in sorted order = len(nums) - 2
        #
        # So we convert:
        # "k-th largest" -> "index of k-th smallest"


          #why this may be better than help on average
        #because it splits search space by hallf everyime
        #but can be n^2 if our pivot is always min or ,max
        
        k = len(nums) - k

        def quickSelect(left, right):
            # We pick the last element as a pivot.
            # A pivot is just a value we use to split the array into:
            # - numbers <= pivot (go to the left side)
            # - numbers > pivot (stay on the right side)
            pivot = nums[right]

            # pointer = where the next smaller element should go
            pointer = left

            # Loop through the subarray (excluding the pivot)
            for i in range(left, right):
                # If current number is smaller than or equal to pivot,
                # move it to the "left side" region
                if nums[i] <= pivot:
                    # swap current number with the number at pointer
                    nums[pointer], nums[i] = nums[i], nums[pointer]
                    pointer += 1

            # After the loop:
            # pointer is the first index where numbers > pivot start.
            # So we place the pivot there.
            nums[pointer], nums[right] = nums[right], nums[pointer]

            # Now pivot is in its FINAL sorted position.
            # All values left of pointer are <= pivot.
            # All values right of pointer are > pivot.

            # If pivot index is bigger than target index k,
            # then the k-th smallest must be on the LEFT side.
            if pointer > k:
                return quickSelect(left, pointer - 1)

            # If pivot index is smaller than k,
            # then the k-th smallest must be on the RIGHT side.
            elif pointer < k:
                return quickSelect(pointer + 1, right)

            # If pointer == k:
            # We found the exact index we were looking for.
            # The pivot is the k-th smallest element.
            else:
                return nums[pointer]

        # Start searching across the whole array
        return quickSelect(0, len(nums) - 1)

# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
        
#         nums = [-n for n in nums]
#         heapq.heapify(nums)
#         for _ in range(k):
#             res = heapq.heappop(nums)
#         return -res
    

