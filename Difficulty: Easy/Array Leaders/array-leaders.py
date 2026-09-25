class Solution:
    def leaders(self, arr):
        max_right = arr[-1]
        res = []
        n = len(arr)
        for i in range(n -1, -1, -1):
            if arr[i] >= max_right:
                res.append(arr[i])
                max_right = arr[i]
        res.reverse()
        return res
        # res = []
        # n = len(arr)
        # for i in range(n):
        #     for j in range(i +1,n):
        #         if arr[i] < arr[j]:
        #             break
        #     else:
        #         res.append(arr[i])
        # return res
                    
        # # code here
        