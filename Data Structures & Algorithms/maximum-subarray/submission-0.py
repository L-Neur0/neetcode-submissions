class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [num for num in nums] 

        for i in range(len(nums) - 2, -1, -1):
            if dp[i+1] + dp[i] >= dp[i]:
                dp[i] += dp[i+1] 

            
        return max(dp)