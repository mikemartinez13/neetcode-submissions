import math

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        subtarget = {}
        for i in range(len(nums)):
            subtarget[target - nums[i]] = i
        
        for j in range(len(nums)):
            if nums[j] in subtarget: 
                if j == subtarget[nums[j]]:
                    continue
                return [j, subtarget[nums[j]]]
        
