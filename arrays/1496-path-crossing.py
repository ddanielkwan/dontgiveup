# Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

# Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        
        tracker = set()
        origin = (0,0)
        tracker.add(origin)
        for direction in path:

            if direction == 'N':
                new_dir = (origin[0], origin[1]+1)
                print(new_dir)
            elif direction =='S':
                new_dir = (origin[0], origin[1]-1)
            elif direction =='E':
                new_dir = (origin[0]+1, origin[1])
            else:
                new_dir = (origin[0]-1, origin[1])
            if new_dir in tracker:

                return True
            origin = new_dir

            tracker.add(origin)
        return False

            
            
            
