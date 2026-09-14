class Solution:
    def checkKthBit(self, n, k):
        # code here
        val =( 1 << k)
        if n & val != 0:
            return True 
        return False