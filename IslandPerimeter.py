class Solution:
    def islandPerimeter(self, grid):
        H, W = len(grid), len(grid[0])        
        area = 0
        for r in range(H):
            for c in range(W):
                if grid[r][c] == 1:
                    area += 4
                    if grid[r-1][c] == 1 and r > 0:
                        area -= 2
                    if grid[r][c-1] == 1 and c > 0:
                        area -= 2
        return area