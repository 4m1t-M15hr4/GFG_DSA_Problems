class Solution:
    def printNos(self, n: int) -> None:
        # Code here
        if n == 0 :
            return 
        print(n, end=' ')
        
        self.printNos(n -1)