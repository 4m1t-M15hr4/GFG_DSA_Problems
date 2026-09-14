class Solution:
    def countBitsFlip(self, a, b):
        #code here
        x = a ^ b
        count = 0
        while x:
            x = x & (x -1)
            count += 1
            
        return count
            