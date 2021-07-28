# https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode:
    def __init__(self):
        # here in dict, key is char and value is the TrieNode
        self.children = {}
        self.endofWord = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        ptr = self.root
        for char in word:
            if char not in ptr.children:
                # key is char and value is the TrieNode
                ptr.children[char] = TrieNode()
            # moving ptr forward
            ptr = ptr.children[char]
            
        ptr.endofWord = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        ptr = self.root
        for char in word:
            if char not in ptr.children:
                return False
            # moving ptr forward
            ptr = ptr.children[char]
        
        # word is present only if ends at the last char
        return ptr.endofWord
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        ptr = self.root
        for char in prefix:
            if char not in ptr.children:
                return False
            # moving ptr forward
            ptr = ptr.children[char]
            
        # we don't care about if word ends here
        return True
        
