from collections import deque, Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        tasks = [A, A, B, B, A]
        A 
        1s + 1w + 1s + 1w + 1s
        n = 1

        return int res = min no of cycles to complete all tasks
        """
        # find count of tasks
        cnt = Counter(tasks)
        max_heap_cnt = [-freq for freq in cnt.values()] # [-3, -2]
        heapq.heapify(max_heap_cnt) # O(n)
        
        # queue for tracking duplicates
        q = deque() # [-cnt, time_when_avlbl]
        time = 0

        while max_heap_cnt or q:
            time += 1
            
            if max_heap_cnt:
                cnt = 1 + heapq.heappop(max_heap_cnt)
                nxt_available_time = time + n
                if cnt < 0:
                    q.append([cnt, nxt_available_time])
            
            if q and q[0][1] == time:
                heapq.heappush(max_heap_cnt, q.popleft()[0])
        return time
