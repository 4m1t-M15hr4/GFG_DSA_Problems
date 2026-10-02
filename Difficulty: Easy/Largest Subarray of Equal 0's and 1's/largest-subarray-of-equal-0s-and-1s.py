class Solution:
    def maxLen(self, arr):
        n = len(arr)
        # code here
        if n <= 1:
            return 0
        max_len = 0
        balance = 0
        first_seen = {}
        first_seen[0] = -1
        for i in range(n):
            if arr[i] == 1:
                balance += 1
            else:
                balance -= 1
            if balance in first_seen:
                length = i -first_seen[balance]
                max_len = max(max_len, length)
            else:
                first_seen[balance] = i
        return max_len
            