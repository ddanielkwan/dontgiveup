# You are given an m x n integer matrix grid​​​, where m and n are both even integers, and an integer k.

# The matrix is composed of several layers, which is shown in the below image, where each color is its own layer:



# A cyclic rotation of the matrix is done by cyclically rotating each layer in the matrix. To cyclically rotate a layer once, each element in the layer will take the place of the adjacent element in the counter-clockwise direction. An example rotation is shown below:


# Return the matrix after applying k cyclic rotations to it.

 

# Example 1:


# Input: grid = [[40,10],[30,20]], k = 1
# Output: [[10,20],[40,30]]
# Explanation: The figures above represent the grid at every state.


class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        
        #k
        # treat each layer like a 1D array (ring) rotate it put it back
        # 1  2  3  4
        # 5  6  7  8
        # 9 10 11 12
        # 13 14 15 16

        # Outer layer is:

        # 1 2 3 4 8 12 16 15 14 13 9 5

        # howmnay layers? layers = min(m, n) // 2
        # Because each layer needs:

        # one top row
        # one bottom row
        # one left column
        # one right column

        # So every layer consumes:

        # 2 rows
        # and
        # 2 columns

        m, n = len(grid), len(grid[0])

        layers = min(m, n) // 2

        for layer in range(layers):

            top = layer
            left = layer
            bottom = m - 1 - layer
            right = n - 1 - layer

            arr = []

            # top row
            for c in range(left, right + 1):
                arr.append(grid[top][c])

            # right col
            for r in range(top + 1, bottom):
                arr.append(grid[r][right])

            # bottom row
            for c in range(right, left - 1, -1):
                arr.append(grid[bottom][c])

            # left col
            for r in range(bottom - 1, top, -1):
                arr.append(grid[r][left])

            # rotate
            k_mod = k % len(arr)

            arr = arr[k_mod:] + arr[:k_mod]

            idx = 0

            # put back

            # top row
            for c in range(left, right + 1):
                grid[top][c] = arr[idx]
                idx += 1

            # right col
            for r in range(top + 1, bottom):
                grid[r][right] = arr[idx]
                idx += 1

            # bottom row
            for c in range(right, left - 1, -1):
                grid[bottom][c] = arr[idx]
                idx += 1

            # left col
            for r in range(bottom - 1, top, -1):
                grid[r][left] = arr[idx]
                idx += 1

        return grid