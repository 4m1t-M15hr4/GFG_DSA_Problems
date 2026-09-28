class Solution:
    def freqSorted(self, arr: list[int]) -> list[list[int]]:
        # code here
        freq = {}
        for i in arr:
            freq[i] = freq.get(i, 0 ) + 1 
        result = []
        for i  in sorted(freq):
            result.append([i , freq[i]])
        return result