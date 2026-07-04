class TrieNode:
    def __init__(self):
        # Each TrieNode stores its outgoing character links.
        self.children = {}
        # True only if a complete inserted word ends at this node.
        self.is_end_of_word = False

class PrefixTree:
    def __init__(self):
        # Just start point of Trie. Usually does not represent real char
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Insert word, char by char, in PrefixTree
        Time: O(L), where L is the length of the word.
        Space: O(L) in the worst case, if all characters create new nodes.
        """
        # temp pointer
        curr = self.root
        for c in word:
            # create TrieNode if char not in PrefixTree
            if c not in curr.children:
                curr.children[c] = TrieNode()
            
            curr = curr.children[c]
        # mark final node as end
        curr.is_end_of_word = True
                
    def search(self, word: str) -> bool:
        """
        Return True only if the full word exists in the Trie.
        Time: O(L), where L is the length of the word.
        Space: O(1), because we only use a pointer.
        """
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]

        return node.is_end_of_word
        
    def startsWith(self, prefix: str) -> bool:
        """
        Return True if any inserted word starts with this prefix.
        Time: O(L), where L is the length of the prefix.
        Space: O(1), because we only use a pointer.
        """
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True
            