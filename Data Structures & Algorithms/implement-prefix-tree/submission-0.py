class PrefixTree:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

    def insert(self, word: str) -> None:
        # self always means the root node. 
        # But as you move down the Trie, you need to check the current node.
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = PrefixTree()
            node = node.children[c]
        node.is_end_of_word = True
                
    def search(self, word: str) -> bool:
        node = self
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_end_of_word
        
    def startsWith(self, prefix: str) -> bool:
        node = self
        
        # first reach the node at end of prefix
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        
        if node.is_end_of_word or node.children:
            return True
        else:
            return False
            

