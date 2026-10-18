class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # I need to find turning point
        if not nums:
            return -1 
        
        l, r = 0, len(nums) - 1
        while l<r:
            m = (l + r)//2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m 
        pivot = l # smallest element

        if nums[pivot] <= target <= nums[-1]:
            return self.binary_search(nums, target, pivot, len(nums) - 1) 
        else:
            return self.binary_search(nums, target, 0, pivot - 1) 

    def binary_search(self, nums, target, l, r) -> int:
        while l <= r: 
            m = (l + r)//2
            if nums[m] == target:
                return m
            elif target > nums[m]:
                l = m + 1
            else:
                r = m - 1

        return -1 