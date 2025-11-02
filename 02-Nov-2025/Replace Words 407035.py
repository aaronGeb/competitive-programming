# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for root in dictionary:
            trie.insert(root)
        replaced = [trie.find_root(word) for word in sentence.split()]
        return " ".join(replaced)
        



class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def find_root(self, word: str) -> str:
        node = self.root
        prefix = []
        for char in word:
            if char not in node.children:
                break
            node = node.children[char]
            prefix.append(char)
            if node.is_end: 
                return "".join(prefix)
        return word  
