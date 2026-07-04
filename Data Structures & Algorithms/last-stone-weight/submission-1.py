class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # [2,3,6,2,4]
        if len(stones) == 1:
            return stones[0]
        stones = [-stone for stone in stones]
        heapq.heapify(stones) # O(n)

        while len(stones) > 1:
            stone1 = -heapq.heappop(stones) #o(1)
            stone2 = -heapq.heappop(stones) #o(1)
            if stone1 > stone2:
                difference = stone1 - stone2
                heapq.heappush(stones, (-difference)) # logn # remember that this is part of while loop
        
        return (-stones[0]) if stones else 0
            