class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """prefix vals for num[i]:
            | 1 | a | a * b | a * b * c |
            postfix vals for num[i]:
            |b * c * d |  c * d | d | 1 |

            for final result we are essentially multiplying accordingly

        """
        output = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix = prefix * nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] = output[i] * postfix
            postfix = postfix * nums[i]
        return output
        