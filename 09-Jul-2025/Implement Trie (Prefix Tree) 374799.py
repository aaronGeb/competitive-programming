# Problem: Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode:
    def __init__(self):
        self.child = {}
        self.is_end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.child:
                node.child[char] = TrieNode()
            node = node.child[char]
        node.is_end = True

        

    def search(self, word: str) -> bool:
        node = self._find_node(word)
        return node is not None and node.is_end
    def startsWith(self, prefix: str) -> bool:
        return self._find_node(prefix) is not None
    def _find_node(self,prefix:str):
        node = self.root
        for char in prefix:
            if char not in node.child:
                return None
            node = node.child[char]
        return node


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)