# Problem: Number of Matching Subsequences - https://leetcode.com/problems/number-of-matching-subsequences/

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = 0  

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.is_end += 1


class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        trie = Trie()
        for w in words:
            trie.insert(w)
        q = deque([(0, trie.root)])

        result = 0
        while q:
            i, node = q.popleft()
            if node.is_end > 0:
                result += node.is_end
                node.is_end = 0  

            for c in range(26):
                child = node.children[c]
                if child is None:
                    continue
                idx = s.find(chr(c + ord('a')), i)
                if idx != -1:
                    q.append((idx + 1, child))

        return result

        