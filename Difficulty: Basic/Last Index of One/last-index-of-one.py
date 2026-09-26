class Solution:
    def lastIndex(self, s: str) -> int:
        res = -1
        
        for i in range(len(s)):
            if s[i] == '1':
                res = i
        return res
        # code here
        
        
