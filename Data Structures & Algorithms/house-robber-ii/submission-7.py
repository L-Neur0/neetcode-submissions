class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return max(nums)
        return max(self.hr_1(nums[1:]), self.hr_1(nums[:-1]))

        

    def hr_1(self, nums) -> int:
        dp = [n for n in nums]
        max_so_far = 0 

        for i in range(2, len(nums)):
            dp[i] = max(max_so_far + dp[i], dp[i], dp[i] + dp[i - 2])
            max_so_far = max(dp[:i -1])

        return max(dp)