class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        dp = [n for n in nums]
        max_res = 0

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + dp[i], max_res + dp[i])
            max_res = max(dp[0:i - 1])
        
        return max(dp)
        