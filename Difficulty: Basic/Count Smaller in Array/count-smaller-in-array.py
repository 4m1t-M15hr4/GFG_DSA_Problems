class Solution:
    def countOfElements(self, x, arr):
        cnt = 0
        for i in arr:
            if i <= x:
                cnt += 1
        return cnt
        # code here

