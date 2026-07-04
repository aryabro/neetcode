from collections import deque, Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Pattern: Heap + Queue / Task Scheduling.

        Problem:
        Given a list of CPU tasks and a cooldown n, return the minimum number
        of time intervals needed to complete all tasks.

        Key idea:
        Always run the task with the highest remaining frequency first.
        Since heapq is a min heap, we store frequencies as negative numbers
        to simulate a max heap.

        Example:
        tasks = ["A", "A", "A", "B", "B"]
        n = 1

        Time: O(T log k), where T is the number of time intervals
              Since k <= 26 for uppercase English letters, this is effectively O(T).

        Space: O(k), for the heap and queue, but it's constant (26 capital letters)
        """
        # find count of tasks and heapify
        cnt = Counter(tasks)
        max_heap_cnt = [-freq for freq in cnt.values()] # [-3, -2], we dont need task names
        heapq.heapify(max_heap_cnt)
        
        # Queue stores tasks that are currently cooling down.
        q = deque() # [-cnt, nxt_available_time]
        time = 0

        while max_heap_cnt or q:
            time += 1
            
            if max_heap_cnt:
                # Pop the highest-frequency task.
                # Because counts are negative, adding 1 means we used one copy.
                curr_cnt = 1 + heapq.heappop(max_heap_cnt)
                nxt_available_time = time + n

                # If the count is still negative, this task has remaining copies.
                # Put it into cooldown queue.
                if curr_cnt < 0:
                    q.append([curr_cnt, nxt_available_time])
            
            # if task as finished cooldown, readd to heap
            if q and q[0][1] == time:
                heapq.heappush(max_heap_cnt, q.popleft()[0])

        return time
