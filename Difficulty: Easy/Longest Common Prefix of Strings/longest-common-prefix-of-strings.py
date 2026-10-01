class Solution:
    def longestCommonPrefix(self, arr):
        # code here
        if not arr:
            return ""
        ans = ""
        for i in range(len(arr[0])):
            for j in range(len(arr)):
                if i >= len(arr[j]) or arr[j][i] !=arr[0][i]:
                    return ans
            ans += arr[0][i]
        return ans