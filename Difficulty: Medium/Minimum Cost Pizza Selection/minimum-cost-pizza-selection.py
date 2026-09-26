class Solution:
    def minimumCost(self, x, s, m, l, cs, cm, cl):
        limit = x + l
        dp = [float('inf')] * (limit + 1)

        dp[0] = 0

        for i in range(limit + 1):

            if dp[i] == float('inf'):
                continue

            if i + s <= limit:
                dp[i + s] = min(dp[i + s], dp[i] + cs)

            if i + m <= limit:
                dp[i + m] = min(dp[i + m], dp[i] + cm)

            if i + l <= limit:
                dp[i + l] = min(dp[i + l], dp[i] + cl)

        res = float('inf')

        for i in range(x, limit + 1):
            res = min(res, dp[i])

        return res

        # code here
