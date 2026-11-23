class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i, num in enumerate(nums):
            res ^= num ^i 

        return res 