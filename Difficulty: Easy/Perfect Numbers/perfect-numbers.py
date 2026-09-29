class Solution:
    def isPerfect(self, n):
        sum = 1
        for i in range(2,int(n **0.5)+ 1):
            if n % i == 0:
                if i * i != n:
                    sum += i+ n // i
                else:
                    sum += i
        return sum == n and n !=1
        # code here 
        # res = 0
        
        # for i in range(1, n):
        #     if n % i ==0:
        #         res += i
        # return res == n