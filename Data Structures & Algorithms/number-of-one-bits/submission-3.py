class Solution:
    def hammingWeight(self, n: int) -> int:
        # shift by 1 with integer division, check with MOD the remainder
        res = 0 

        while n: 
            res += n % 2 
            n = n // 2

        return res