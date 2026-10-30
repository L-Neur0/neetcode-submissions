class Solution:
    def rob(self, nums: List[int]) -> int:
        max_seen = 0 
        money = [num for num in nums]
        max_seen = money[0]

        for i in range(2, len(nums)):
            money[i] += max_seen
            max_seen = max(max_seen, money[i - 1])

        return max(money)
