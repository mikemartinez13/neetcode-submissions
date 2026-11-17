class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points_l2 = [((p[0]**2 + p[1]**2)**0.5, p) for p in points]

        heapq.heapify_max(points_l2)

        while len(points_l2) > k:
            heapq.heappop_max(points_l2)
        
        res = []
        while len(points_l2)>0:
            res.append(heapq.heappop_max(points_l2)[1])

        return res