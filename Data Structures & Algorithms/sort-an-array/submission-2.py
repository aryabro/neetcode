class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergesort(arr, l, r):
            # base case
            if l >= r:
                return
            
            m = (l + r) // 2
            # recursively sort left and right halfs
            mergesort(arr, l, m)
            mergesort(arr, m+1, r)

            # join both halves
            merge(arr, l, m, r) 
         
        def merge(arr, L, M, R):
            left, right = arr[L:M+1], arr[M+1:R+1]
            i, j = 0,0
            k = L

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                arr[k] = left[i]
                k += 1
                i += 1 
            
            while j < len(right):
                arr[k] = right[j]
                k += 1
                j += 1 
        
        mergesort(nums, 0, len(nums) - 1)
        return nums
