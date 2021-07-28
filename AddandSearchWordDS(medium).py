class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofWord = False
        

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        ptr = self.root
        for char in word:
            if char not in ptr.children:
                ptr.children[char] = TrieNode()
            
            ptr = ptr.children[char]
            
        ptr.endofWord = True
        

    def search(self, word: str) -> bool:
        return self.searchDFS(self.root, word)
    
    
    def searchDFS(self, node: TrieNode, word: str) -> bool:
        for i in range(len(word)):
            char = word[i]
            # if dot then check all the children of node at char
            if char == ".":
                for charKey in node.children:
                    # passing node at charKey and rest of word
                    if self.searchDFS(node.children[charKey], word[i+1:]):
                        return True
                # if there are no children
                return False
            
            elif char not in node.children:
                return False
            
            # moving forward (still inside loop)
            node = node.children[char]
        
        # returns true if word properly ends
        return node.endofWord
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)