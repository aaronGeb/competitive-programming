# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def is_valid_word(self, word):
        node = self.root
        for ch in word:
            node = node.children[ch]
            if not node.is_end:
                return False
        return True

class Solution:
    def longestWord(self, words: list[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)

        longest = ""
        for word in words:
            if trie.is_valid_word(word):
                if len(word) > len(longest) or (len(word) == len(longest) and word < longest):
                    longest = word
        return longest