#Approach
#Explore all the paths and if that path has the obstacles less than or equal to k return. To find the min path using BFS


#Complexities
#Time: O(m*n)
#Space: O(m*n)


from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        queue = []

        queue.append((0, 0, k, 0))
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        visited = set([(0, 0, k)])
        while queue:
            x, y, remK, steps = queue.pop(0)
            if x == len(grid) - 1 and y == len(grid[0]) - 1:
                return steps
            for r, c in directions:
                nr = x + r
                nc = y + c
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    newK = remK - grid[nr][nc]
                    if newK >= 0 and (nr, nc, newK) not in visited:
                        queue.append((nr, nc, newK, steps + 1))
                        visited.add((nr, nc, newK))

        return -1





