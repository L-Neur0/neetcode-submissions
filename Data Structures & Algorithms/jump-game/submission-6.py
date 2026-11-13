class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * (len(nums))
        dp[0] = True 

        for i in range(len(nums)):
            for j in range(1, nums[i]+1):
                if (i + j) <= (len(nums) -1) and dp[i]:
                    dp[i + j] = dp[i]

            
        return dp[len(nums) - 1]

