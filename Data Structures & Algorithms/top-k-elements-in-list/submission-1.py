from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count = defaultdict(int)

        # for i in range(len(nums)):
        #     count[nums[i]]+=1

        # sorted_count = dict(sorted(count.items(), key=lambda item: item[1], reverse = True))
        # for key, value in count.items():
        
        # This is the naive solution, using hash arrays

        # However, we can use bucket sort: 

        # map the counts of each number of occurrences, and store all values that occur x times at index x. 

        count = {}
        freq = [[] for _ in range(len(nums)+1)]

        for n in nums: 
            count[n] = 1+count.get(n, 0)
        
        for n, c in count.items():
            freq[c].append(n)

        res = []

        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        


