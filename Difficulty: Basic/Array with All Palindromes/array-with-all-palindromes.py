def ispali(n):
    s = str(n)
    return s == s[::-1]
        
class Solution:
    def isPalinArray(self, arr):
        for num in arr:
            if not ispali(num):
                return False
        return True
         # code here
         