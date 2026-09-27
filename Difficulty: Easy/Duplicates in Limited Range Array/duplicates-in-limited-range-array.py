class Solution:
    def findDuplicates(self, arr):
        # code here
        freq = {}
        ans = []
        for i in arr:
            if i in freq:
                freq[i] +=1
            else:
                freq[i] = 1
        for i, count in  freq.items():
            if count > 1:
                ans.append(i)
        return ans