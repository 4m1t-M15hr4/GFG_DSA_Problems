class Solution:
    def factorial(self, n: int) -> int:
        factorial = 1
        for i in range(1, n+1):
            factorial = factorial *i
        return factorial
        
        