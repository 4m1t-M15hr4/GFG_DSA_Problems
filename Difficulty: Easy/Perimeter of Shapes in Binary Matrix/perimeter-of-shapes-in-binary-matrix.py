from typing import Lis
class Solution:
    def findPerimeter(self, mat: List[List[int]]) -> int:
        # code here
            
        
        n = len(mat)
        m = len(mat[0])
        perimeter = 0

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    continue

                # Check all four sides of the current 1 cell.
                for dr, dc in directions:
                    ni = i + dr
                    nj = j + dc

                    # Count the side if it is exposed.
                    if (ni < 0 or ni >= n or
                        nj < 0 or nj >= m or
                        mat[ni][nj] == 0):
                        perimeter += 1

        return perimeter
