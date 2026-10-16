class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = defaultdict(int)

        for i in range(len(nums)):
            lookup[nums[i]] = i
        
        for i in range(len(nums)):
            compl = target - nums[i]
            if compl in lookup.keys() and lookup[compl] != i:
                return [i, lookup[compl]]