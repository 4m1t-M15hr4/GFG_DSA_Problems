class solution:
    def uniqueNumbers(self, l, r):
        # code here
    
        res = []
        while l <= r:
            if self.un(l):
                res.append(l)
            l += 1
        return res
            

    def un(self, nums):
        seen = set()
        while nums > 0:
            digit = nums% 10
            if digit in seen: return False
            
            seen.add(digit)
            nums //= 10
        return True