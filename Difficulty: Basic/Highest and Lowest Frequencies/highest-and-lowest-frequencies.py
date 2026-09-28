from collections
import defaultdict
class Solution:
    def findDiff(self, arr):
        n = len(arr)
        
        mp = defaultdict(int)
        for i in range(n):
            mp[arr[i]] +=1
        maxf = 0
        minf = n
        for x in mp.values():
            maxf = max(maxf, x)
            minf = min(minf, x)
        return (maxf - minf)
        
    
    
    
    