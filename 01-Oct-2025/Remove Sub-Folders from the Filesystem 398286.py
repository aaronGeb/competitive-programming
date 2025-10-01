# Problem: Remove Sub-Folders from the Filesystem - https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        for key, val in enumerate(folder):
            trie.insert(key, val)
        return [folder[val] for val in trie.search()]

class Trie:
    def __init__(self):
        self.children = {}
        self.folder_id = -1  

    def insert(self, idx: int, folder: str) -> None:
        node = self
        for part in folder.split('/')[1:]:  
            node = node.children.setdefault(part, Trie())
        node.folder_id = idx

    def search(self):
        result = []

        def dfs(node: "Trie"):
            if node.folder_id != -1:
                result.append(node.folder_id)
                return
            for child in node.children.values():
                dfs(child)

        dfs(self)
        return result
