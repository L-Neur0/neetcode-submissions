class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 4: 
            return max(nums)
        houses1 = nums[:-1]
        houses2 = nums[1:]

        arr1 = [n for n in houses1]
        arr2 = [n for n in houses2]

        max_seen = houses1[0]

        for i in range(2, len(houses1)):
            houses1[i] += max_seen 
            max_seen = max(max_seen, houses1[i - 1])

        max_seen = houses2[0]

        for i in range(2, len(houses2)):
            houses2[i] += max_seen 
            max_seen = max(max_seen, houses2[i - 1])
        return max(max(houses1), max(houses2))
