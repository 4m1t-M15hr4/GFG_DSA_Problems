class Solution:
    def binarySubstring(self, s):
        #code here
        ones = 0
        for i in range(len(s)):
            if s[i] == '1':
                ones +=1
        return ( ones *(ones -1 )) // 2