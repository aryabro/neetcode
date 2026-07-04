class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs_backtrack(i:int, cur:list, total:int ):
            if total == target:
                res.append(cur.copy())
                return

            if i >= len(nums) or total > target:
                return
            
            # considering the val at i
            cur.append(nums[i])
            new_total = total + nums[i]
            dfs_backtrack(i, cur, new_total)

            # NOT considering the val at i 
            cur.pop()
            dfs_backtrack(i + 1, cur, total)

        dfs_backtrack(0, [], 0)
        return res