# You are playing a simplified PAC-MAN game on an infinite 2-D grid. You start at the point [0, 0], and you are given a destination point target = [xtarget, ytarget] that you are trying to get to. There are several ghosts on the map with their starting positions given as a 2D array ghosts, where ghosts[i] = [xi, yi] represents the starting position of the ith ghost. All inputs are integral coordinates.

# Each turn, you and all the ghosts may independently choose to either move 1 unit in any of the four cardinal directions: north, east, south, or west, or stay still. All actions happen simultaneously.

# You escape if and only if you can reach the target before any ghost reaches you. If you reach any square (including the target) at the same time as a ghost, it does not count as an escape.

# Return true if it is possible to escape regardless of how the ghosts move, otherwise return false.


class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        # you escape only if YOU reach target strictly earlier than EVERY ghost
        #manhattan distance

        # On an empty grid, the only thing that matters is:
# who can reach the target faster, no walls no obstacles
        # your shortest distance to target
        my_distance = abs(target[0]) + abs(target[1])

        for ghost_x, ghost_y in ghosts:

            # ghost shortest distance to target
            ghost_distance = (
                abs(ghost_x - target[0]) +
                abs(ghost_y - target[1])
            )
# so this soltuon is just saying, calcualte my distanve needed, calcualte all ghsots dsitance needed, and if any of ghost sdiistance is shorter then i cant make it
            # ghost can reach first or same time
            if ghost_distance <= my_distance:
                return False

        return True