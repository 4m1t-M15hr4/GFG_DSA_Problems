class Solution:
	def countOddEven(self, arr):
		#Code here
		cntodd = 0
		cnteven = 0
		for num in arr:
		    if num % 2 == 0:
		        cnteven += 1
		    else:
		        cntodd += 1
		        
		        
        return cntodd, cnteven