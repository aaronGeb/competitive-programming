# Problem: Top K Frequent Words - https://leetcode.com/problems/top-k-frequent-words/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        trie = Trie()
        for word in count:
            trie.insert(word)
        candidates = list(trie.traverse())
        
       
        candidates.sort(key=lambda w: (-count[w], w))
        
        return candidates[:k]
     

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        node.word = word
    
    def traverse(self, node=None):
        if node is None:
            node = self.root
        if node.is_end:
            yield node.word
        for char in sorted(node.children.keys()):  
            yield from self.traverse(node.children[char])

