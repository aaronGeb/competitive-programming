# Problem: Search Suggestions System - https://leetcode.com/problems/search-suggestions-system/

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = TrieNode()
        products.sort()
        for product in products:
            node = root
            for ch in product:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
                if len(node.suggestions) < 3:
                    node.suggestions.append(product)

        res = []
        node = root
        for ch in searchWord:
            if node and ch in node.children:
                node = node.children[ch]
                res.append(node.suggestions)
            else:
                node = None
                res.append([])
        return res
        
class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []