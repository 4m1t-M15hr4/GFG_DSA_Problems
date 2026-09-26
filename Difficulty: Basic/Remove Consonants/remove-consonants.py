class Solution:
    def remConsonants(self, s):
        # code here
        ans = ""
        for i in s:
            if i in "aeiou" or i in "AEIOU":
                ans += i
        return ans