class Solution:
    def rotate(self, arr: list[int]) -> None:
        # code here
        i, j = 0, len(arr) - 1 
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            
        