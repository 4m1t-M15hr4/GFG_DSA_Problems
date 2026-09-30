class Solution:
    def maxIndexDiff(self, arr):
        # code here
        n = len(arr)
        st = []
        for i in range(n):
            if not st or arr[st[-1]] > arr[i]:
                st.append(i)
        ans = 0
        
        for j in range(n -1, -1,-1):
            while st and arr[st[-1]] <= arr[j]:
                ans = max(ans, j -st[-1])
                st.pop()
        return ans

        
        