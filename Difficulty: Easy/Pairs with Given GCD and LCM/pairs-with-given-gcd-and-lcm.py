from math import gcd, sqrt


class Solution:
    def pairCount(self, x, y):
        if y % x != 0:
            return 0
        n = y // x
        if n == 1:
            return 1
        res = 0
        for i in range(1, int(sqrt(n)) + 1):
            if n % i == 0:
                j = n // i
                if gcd(i,j) == 1:
                    if i == j:
                        res += 1
                    else:
                        res += 2
        return res
        """code here"""
