class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # first thing to note, we should keep track of how many of each character there is. 
        # always try to schedule the most frequent character greedily

        # we can use the maxheap to do this to figure out which is the most frequent one, continuously
        # we also use a queue because we know there is some idle time, so we keep track of what time we can add a certain trask back to the maxheap. 

        count = Counter(tasks) # creates a hash map
        maxHeap = [cnt for cnt in count.values()]

        heapq.heapify_max(maxHeap)

        time = 0
        q = deque() # pairs of [cnt, idleTime]

        while maxHeap or q: # while nonempty or there are tasks in the queue
            time +=1 

            if maxHeap:
                cnt = heapq.heappop_max(maxHeap) -1 # get the frequency
                if cnt:
                    q.append([cnt, time + n]) # get the time it will be available again
            
            if q and q[0][1] == time:
                heapq.heappush_max(maxHeap, q.popleft()[0]) # just simply add this back to the max heap
        
        return time