class Trie:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.word = ''


class Solution:
    def __init__(self):
        self.root = Trie()

    def createTrie(self, wordList):
        for word in wordList:
            node = self.root
            for c in word:
                if c not in node.children:
                    node.children[c] = Trie()
                node = node.children[c]
            node.isWord = True
            node.word = word

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        self.createTrie(dictionary)
        memo = {}
        def util(index):
            if index >= len(s):
                return 0
            if index in memo:
                return memo[index]
            # Skip current character -> it becomes extra
            skip = 1 + util(index + 1)

            # Try matching a dictionary word starting at index
            take = float('inf')
            node = self.root

            for i in range(index, len(s)):
                if s[i] not in node.children:
                    break

                node = node.children[s[i]]

                if node.isWord:
                    take = min(take, util(i + 1))
            memo[index] = min(skip, take)
            return min(skip, take)

        return util(0)