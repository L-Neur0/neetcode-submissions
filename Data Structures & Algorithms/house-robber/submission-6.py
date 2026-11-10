class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [n for n in nums]
        max_so_far = nums[0]

        for i in range(2, len(nums)):
            dp[i] = max(dp[i], dp[i] + dp[i - 2], max_so_far + dp[i])
            max_so_far = max(dp[:i-1])
        
        return max(dp)