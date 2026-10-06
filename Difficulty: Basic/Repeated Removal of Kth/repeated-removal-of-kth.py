class Solution:

    def getCandidate(self, n, k):
        res = 1
        
        while res <= n // k:
            res *= k
        return res