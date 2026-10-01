from collections import deque
class Solution:
    def minTime(self, duration, dependencies):
        # code here
        n = len(duration)

         
        adj = [[] for _ in range(n)]
        indegree = [0] * n

        for edge in dependencies:
            adj[edge[0]].append(edge[1])
            indegree[edge[1]] += 1

        finishTime = duration[:]

        q = deque()

        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        visited = 0
        res = 0

        while q:

            node = q.popleft()

            visited += 1
            res = max(res, finishTime[node])

             
            for next in adj[node]:

                finishTime[next] = max(
                    finishTime[next],
                    finishTime[node] + duration[next]
                 )

                indegree[next] -= 1

                if indegree[next] == 0:
                    q.append(next)

        
        if visited != n:
            return -1

        return res
