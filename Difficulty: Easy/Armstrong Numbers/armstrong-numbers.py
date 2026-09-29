class Solution:
    def armstrongNumber (self, n):
        # code here 
        s = str(n)
        ni = len(s)
        res = 0
        for i in s:
            res += int(i) ** ni
        return res == n