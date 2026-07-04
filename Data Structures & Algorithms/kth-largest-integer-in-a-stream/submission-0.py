import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]): # k = 3, nums = [6,2,8,1,4,7]
        self.k = k
        self.minHeap = nums
        heapq.heapify(nums)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
        
    def add(self, val: int):
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]