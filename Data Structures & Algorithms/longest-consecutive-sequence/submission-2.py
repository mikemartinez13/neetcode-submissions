class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # naive solution is sorting. 

        # most important thing is to identify "what makes a sequence"

        # each sequence has a start value, where the start value has NO left neighbor. 

        # Take the initial array and see if it has a set. CHECK if we have a left neighbor

        # Find the numbers that are a START of the sequence, and we do this by conerting the initial array into a set, and finding if we have left neighbors. 

        numSet = set(nums)

        longest = 0

        for n in nums:
            # check if it's the start of a sequence
            if (n-1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)

        return longest
