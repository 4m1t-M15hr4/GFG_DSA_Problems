class Solution:
    def largestSubsquare(self, mat):
        # code here
        n = len(mat)

            
        right = [[0] * n for _ in range(n)]
        down = [[0] * n for _ in range(n)]

            
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if mat[i][j] == 'X':
                    right[i][j] = 1 if j == n - 1 else right[i][j + 1] + 1
                    down[i][j] = 1 if i == n - 1 else down[i + 1][j] + 1

        maxSize = 0


        for i in range(n):
            for j in range(n):

                    
                maxSide = min(right[i][j], down[i][j])

                   
                for side in range(maxSide, 0, -1):

                        
                    if right[i + side - 1][j] >= side and \
                                down[i][j + side - 1] >= side:
                        maxSize = max(maxSize, side)
                        break

        return maxSize