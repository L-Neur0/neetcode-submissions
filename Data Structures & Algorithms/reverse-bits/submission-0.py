class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0 

        for i in range(0, 32): 
            last = n % 2 
            res = res * 2 + last 
            n = n >> 1

        return res