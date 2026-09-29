# def f(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return f(n -2) + f(n-1)
class Solution:
    def fibonacciNumbers(self, n: int) -> list[int]:
        dp = [0] * n
        if n >= 1:
            dp[0] = 0
        if n >= 2:
            dp[1] = 1
        for i in range(2, n):
            dp[i] = dp[i -1] + dp [i -2]
        return dp
            
        # code here
        # ans = []
        # for i in range(n):
        #     ans.append(f(i))
        # return ans