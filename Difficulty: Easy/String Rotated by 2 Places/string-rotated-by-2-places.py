class Solution:
    def isRotated(self,s1,s2):
        if len(s1) != len(s2):
            return False
        if len(s1) <= 2 or len(s2) <= 2:
            return s1 == s2
        s = ""
        s3 =""
        #code here
        s = s2[2:] + s2[:2]
        s3 = s2[-2:] + s2[:-2]
        return s1 == s or s1 == s3
           