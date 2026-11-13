class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #[-4,-1,-1,0,1,2]
        # notice that at each index, the sublist we're looking for is then just trying to solve the two sum II input array is sorted. Since best we can do is O(n^2), it's ok to sort at the beginning. 
        # -3, -3, 1, 2, 3, 4. Notice here, if we get to -3, if left neighbor is also -3, then we'll get the same duplicate. So we say we computed all combinations with -3, and we SKIP. 

        # nums.sort()

        # triplets = set()

        # for i in range(len(nums)):
        #     subnums = nums[:i] + nums[i+1:]

        #     left = 0
        #     right = len(subnums)-1
        #     target = -nums[i]

            
        #     #print(subnums, target)

        #     while left < right: 
        #         if subnums[left] + subnums[right] > target:
        #             right -=1
        #         elif subnums[left] + subnums[right] < target:
        #             left +=1
        #         else:
        #             triplet = [subnums[left], subnums[right], -target]
        #             triplet.sort()
        #             triplet = tuple(triplet)
        #             #print("triplet found!", triplet)
        #             triplets.add(triplet)
        #             break

        
        # return [list(trip) for trip in triplets]



        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            
            l, r = i+1, len(nums)-1

            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -=1 
                elif threeSum < 0:
                    l +=1 
                else:
                    res.append([a, nums[l], nums[r]])
                    l+=1 
                    # how do we update the pointers here?
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
                    # [-2, -2, 0, 0, 2, 2]
            
        return res