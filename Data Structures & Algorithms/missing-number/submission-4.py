class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        end = len(nums)
        nums_set = set(nums)
        for i in range(0, end + 1):
            if i not in nums:
                return i
        return 0