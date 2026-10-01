class Solution:
    def insertAtIndex(self, arr, index, val):
        
        # return arr[:index] + [val] +arr[index:]
        # new_arr = []
        
        # for i in range(len(arr)):
        #     if i == index:
        #         new_arr.append(val)
        #     new_arr.append(arr[i])
        # if index == len(arr):
        #     new_arr.append(val)
        # return new_arr
        
        # # arr.insert(index, val)
        arr.append(0)
        for i in range(len(arr)-1,index,-1):
            arr[i] = arr[i - 1]
            
        arr[index]= val
        return arr
        