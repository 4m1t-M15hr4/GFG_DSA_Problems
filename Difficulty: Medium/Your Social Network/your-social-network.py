class Solution:
    def socialNetwork(self, arr):
        # code here
        n = len(arr) + 1
        ans = []

        for i in range(2, n + 1):
            path = []
            curr = i
            while curr != 1:
                curr = arr[curr - 2]
                path.append(curr)
            distance = len(path)

            for j in range(len(path) - 1, -1, -1):
                ans.append([i, path[j], distance])
                distance -= 1

        return ans
