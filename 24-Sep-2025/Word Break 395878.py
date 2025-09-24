# Problem: Word Break - https://leetcode.com/problems/word-break/description/

class TrieNode:
    def __init__(self):
        self.child = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.child:
                node.child[char] = TrieNode()
            node = node.child[char]
        node.is_end = True 

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.child:
                return False
            node = node.child[char]
        return node.is_end
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        #return trie.search(s)
        n = len(s)
        dp = [False]*(n+1)
        dp[0] =  True
        for  i in range(n):
            if not  dp[i]:
                continue
            node = trie. root
            k = i
            while k<n and s[k] in  node.child:
                node= node.child[s[k]]
                k +=1
                if node.is_end:
                    dp[k]= True
        return dp[n]
