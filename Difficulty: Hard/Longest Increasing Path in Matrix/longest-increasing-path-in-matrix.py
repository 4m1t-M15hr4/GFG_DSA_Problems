from collections import deque
class Solution:
    def longIncPath(self, matrix, n, m):
        # code here
        
        n = len(matrix)
        m = len(matrix[0])

       
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        degree = [[0 for _ in range(m)] for _ in range(n)]
     
        for i in range(n):
            for j in range(m):
                for dx, dy in dir:
                    x, y = i + dx, j + dy
                    if 0 <= x < n and 0 <= y < m and matrix[x][y] < matrix[i][j]:
                        degree[i][j] += 1

        q = deque()
        for i in range(n):
            for j in range(m):
                if degree[i][j] == 0:
                    q.append((i, j))

        ans = 0
        while q:
            ans += 1
            for _ in range(len(q)):
                x1, y1 = q.popleft()
                for dx, dy in dir:
                    x, y = x1 + dx, y1 + dy
                    if 0 <= x < n and 0 <= y < m and matrix[x][y] > matrix[x1][y1]:
                        degree[x][y] -= 1
                        if degree[x][y] == 0:
                            q.append((x, y))
        return ans