class Solution:
    def hasTripletSum(self, arr, target):
        n = len(arr)
        arr.sort()
        for i in range(n - 2):
            l = i +1
            r = n -1
            resum = target - arr[i]
            while l < r:
                if arr[l] + arr[r] == resum:
                    return True
                elif arr[l] + arr[r] < resum:
                    l +=1
                else:
                    r -= 1
        return False
            
        # n = len(arr)
        # for i in range(n-2):
        #     for j in range(i +1, n-1):
        #         for x in range(j + 1, n):
        #             if arr[i] + arr[j] + arr[x] == target:
        #                 return True
        # return False
                    