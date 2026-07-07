class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)

        # make array length "len(s) + 1" as if i reaches end, that means word is over
        is_segmentable_till = [True] + [False] * len(s)
    
        for i in range(1, len(s) + 1):
            for j in range(i):
                if is_segmentable_till[j] and s[j:i] in word_set:
                    is_segmentable_till[i] = True
                    break
        
        return is_segmentable_till[-1]
