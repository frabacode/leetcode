class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):
            missing = target - num

            if missing in seen:
                return [seen[missing], i]
        
            seen[num] = i
        
