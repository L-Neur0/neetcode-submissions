class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r: 
            m = (r + l)//2
            if nums[m] <= nums[r]:
                # orderd, it has to be in the other one
                r = m 
            else:
                # not ordered, it is in here
                l = m + 1
        return nums[l]