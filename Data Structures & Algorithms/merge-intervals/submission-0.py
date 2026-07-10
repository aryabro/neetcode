class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key=lambda x: x[0])
        for interval in intervals:
            # if res is empty or there's no overlap of the
            # current interval with prev, directly append it
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
                
            # if there's overlap, merge current and prev
            else:
                res[-1][1] = max(res[-1][1], interval[1])
            
        return res