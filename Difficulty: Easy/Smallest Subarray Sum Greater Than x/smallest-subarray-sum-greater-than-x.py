class Solution:
    def smallestSubWithSum(self, x, arr):
        left = 0
        window_sum = 0
        ans = float('inf')

        for right in range(len(arr)):
            window_sum += arr[right]

            while window_sum > x:
                ans = min(ans, right - left + 1)

                window_sum -= arr[left]
                left += 1

        return 0 if ans == float('inf') else ans