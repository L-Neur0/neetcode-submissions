class TrieNode:
    def __init__(self):
            self.children = {}
            self.is_word = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        node = self.root 
        for char in word: 
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True 


    def search(self, word: str) -> bool:
        cur = self.root 

        for char in word: 
            if char not in cur.children:
                return False
            else: 
                cur = cur.children[char]
        return cur.is_word
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root 

        for char in prefix:
            if char not in cur.children:
                return False 
            else: 
                cur = cur.children[char]
        return True 
