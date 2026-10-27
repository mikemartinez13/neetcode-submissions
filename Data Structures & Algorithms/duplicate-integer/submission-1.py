class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        start_set = set()

        for i in range(len(nums)):
            if nums[i] in start_set:
                return True
            else:
                start_set.add(nums[i])

        return False