class Solution:
    def areAnagrams(self, s1, s2):
        fre1 = {}
        fre2 = {}
        
        for i in s1:
            fre1[i] = fre1.get(i, 0) +1
        
        for j in s2:
            fre2[j] = fre2.get(j, 0) + 1
            
        return fre1 == fre2
     
       
       
       
       