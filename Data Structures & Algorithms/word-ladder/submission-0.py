from collections import defaultdict, deque
class Solution:
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Pattern: BFS on an implicit graph.

        Problem:
        Given a beginWord, endWord, and wordList, find the length of the shortest
        transformation sequence from beginWord to endWord.
        Each transformation can change exactly one character, and every intermediate
        word must exist in wordList.

        Key idea:
        Treat each word as a node in a graph.
        Two words are connected if they differ by exactly one character.

        Instead of comparing every word with every other word, create wildcard patterns.
        Example:
            "hot" -> "*ot", "h*t", "ho*"

        Words that share the same pattern are one letter apart.
        Example:
            "*ot" -> ["hot", "dot", "lot"]

        Then run BFS from beginWord because BFS finds the shortest path in an
        unweighted graph.

        Time: O(n * m^2)
              n = number of words
              m = length of each word
              For each word, we generate m patterns, and slicing each pattern costs O(m).

        Space: O(n * m)
               We store m patterns for each word in the neighbors map.
        """
        if endWord not in wordList:
            return 0

        wordList.append(beginWord)
        # basically we want to create a graph that connects all words 
        # with a difference of one char with each other
        # Example:
        # "hot" creates:
        #   "*ot" -> ["hot", "dot", "lot"]
        #   "h*t" -> ["hot"]
        #   "ho*" -> ["hot"]

        # create a hashmap that stores all possible next words for words in the wordList
        # e.g. for dict["*ot"] = [all words that have ot and * is wild card]
        neighbors = collections.defaultdict(list)

        # generate all possible patterns to the neighbors hashmap
        for w in wordList:
            for j in range(len(w)):
                pattern = w[:j] + "*" + w[j+1:]
                neighbors[pattern].append(w)
        
        # prepare for bfs
        q = deque([beginWord])
        visit = set([beginWord]) # track visited words
        res = 1
        while q:
            # process one BFS level at a time
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res

                # if word not reached, generate all patterns for current word
                # and check if it can be visited through BFS
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neighbor_word in neighbors[pattern]:
                        if neighbor_word not in visit:
                            visit.add(neighbor_word)
                            q.append(neighbor_word)
            
            # Increase transformation length after finishing one BFS level
            res += 1
        
        return 0 # no valid path found
        