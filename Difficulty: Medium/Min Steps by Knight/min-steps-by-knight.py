class Solution:
	def minStepToReachTarget(self, knightPos: list[int], targetPos: list[int], n: int) -> int:
		#Code here
		
        x = knightPos[0] - 1
        y = knightPos[1] - 1
        tx = targetPos[0] - 1
        ty = targetPos[1] - 1
        
        dx = [2, 2, -2, -2, 1, 1, -1, -1]
        dy = [1, -1, 1, -1, 2, -2, 2, -2]
        
        q = deque()
        
        visited = [[False] * n for _ in range(n)]
        
        q.append((x, y, 0))
        visited[x][y] = True
        
        while q:
            x, y, steps = q.popleft()
        
            if x == tx and y == ty:
                return steps
        
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
        
                if (nx >= 0 and nx < n and ny >= 0 and ny < n
                        and not visited[nx][ny]):
        
                    visited[nx][ny] = True
        
                    q.append((nx, ny, steps + 1))
        
        return -1
