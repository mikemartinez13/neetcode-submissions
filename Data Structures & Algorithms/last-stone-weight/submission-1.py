class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_heap = stones.copy()
        heapq.heapify_max(stones_heap)
        while len(stones_heap) >1:

            x = heapq.heappop_max(stones_heap)
            y = heapq.heappop_max(stones_heap)

            if x == y:
                continue
            else:
                heapq.heappush_max(stones_heap, x-y)
        
        if len(stones_heap) > 0:
            return stones_heap[0]
        return 0