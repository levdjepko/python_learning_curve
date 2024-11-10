from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        if rows == 0:
            return -1

        # keeping track of fresh oranges
        fresh_count = 0
        # create a queue for rotten oranges:
        rotten = deque()

        # go over each cell first and keep track of all the fresh and rotten oranges
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    # rotten orange
                    rotten.append((row, col))
                elif grid[row][col] == 1:
                    # fresh one
                    fresh_count += 1
        # now, iterate over the entire set ant track time it takes to make all the oranges rotten
        minute = 0

        while rotten and fresh_count > 0:

            # update the number of minutes passed
            # it is safe to update the minutes by 1, since we visit oranges level by level in BFS traversal.
            minute += 1
            
            # process rotten oranges on the current level
            for _ in range(len(rotten)):
                x, y = rotten.popleft()
                
                # visit all the adjacent cells
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    # calculate the coordinates of the adjacent cell
                    xx, yy = x + dx, y + dy
                    # ignore the cell if it is out of the grid boundary
                    if xx < 0 or xx == rows or yy < 0 or yy == cols:
                        continue
                    # ignore the cell if it is empty '0' or visited before '2'
                    if grid[xx][yy] == 0 or grid[xx][yy] == 2:
                        continue
                        
                    # update the fresh oranges count
                    fresh_count -= 1
                    2
                    # mark the current fresh orange as rotten
                    grid[xx][yy] = 2
                    
                    # add the current rotten to the queue
                    rotten.append((xx, yy))

        return minute if fresh_count == 0 else -1
