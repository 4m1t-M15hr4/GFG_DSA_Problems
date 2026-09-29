class Solution:
    def reverses(self, s):
        # code here
        n = len(s)
        s = list(s)
        l = 0
        r = n - 1
        while l < r:
            if s[l] ==' ':
                l +=1
                continue
            elif s[r] ==' ':
                r -= 1
                continue
            else:
                s[l], s[r] = s[r], s[l]
                l +=1
                r -=1
        return "".join(s)