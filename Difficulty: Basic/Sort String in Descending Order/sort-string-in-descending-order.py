class Solution:
    def reverseSort(self, s): 
        # code here
        return "".join(sorted(s, reverse= True))