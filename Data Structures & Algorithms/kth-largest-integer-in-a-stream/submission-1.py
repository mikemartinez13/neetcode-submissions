class KthLargest:
    # whenever calling the function, you're guaranteed to have at least k elements
    # min heap of size k, required to be of size k
    # add/pop in logn
    # get min value in O(1)
    # notice since we never remove, we only need a heap of size k total
    def __init__(self, k: int, nums: List[int]):
        # minHeap with K largest integers
        self.minHeap, self.k = nums, k 
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > self.k: 
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        return self.minHeap[0] # always the minimum value

