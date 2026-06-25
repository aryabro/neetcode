class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        1. Sorting:
        Count the frequency of each number using a hash map. Then sort the unique numbers by their frequency.
        Return the top k most frequent numbers.
        Time complexity is O(n log n), where n is the length of nums.
        Space complexity is O(n).

        2. Min-Heap:
        Count the frequency of each number using a hash map. Then use a min-heap of size k to keep track
        of the k most frequent numbers.
        Time complexity is O(n log k).
        Space complexity is O(n + k).

        3. Bucket Sort:
        Count the frequency of each number using a hash map. Then create a frequency array where the index
        represents the frequency, and each index stores a list of numbers that appear that many times.
        Since the max frequency possible is len(nums), the bucket list size should be len(nums) + 1.
        Then iterate from the highest frequency to the lowest and collect numbers until we have k elements.
        Time complexity is O(n).
        Space complexity is O(n).
        """

        # count stores how many times each number appears in nums
        count = {}

        # freq is the bucket list
        # index = frequency/count of a number
        # value = list of numbers that appear index number of times
        # size is len(nums) + 1 because a number can appear up to len(nums) times
        freq = [[] for i in range(len(nums) + 1)]

        # this builds the frequency map for every number in nums
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # this places each number into the bucket matching its frequency
        # example: if num appears 3 times, it goes into freq[3]
        for num, cnt_of_num in count.items():
            freq[cnt_of_num].append(num)

        # result stores the top k frequent elements
        result = []

        # iterate from highest possible frequency to lowest frequency
        # high frequency numbers are toward the end of freq
        for i in range(len(freq) - 1, 0, -1):

            # add all numbers that appear i times
            for num in freq[i]:
                result.append(num)

                # once result has k elements, return it
                if len(result) == k:
                    return result