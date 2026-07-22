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
            print(word, node.isWord)
        return
        

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.createTrie(wordDict)
        curr = []
        res = []
        def util(index, node):
            # print(curr)
            if index >= len(s):
                res.append(' '.join(curr))
                return
            
            for i in range(index, len(s)):
                val = s[i]
                if val not in node.children:
                    return
                if node.children[val].isWord:
                    curr.append(node.children[val].word)
                    util(i + 1, self.root)
                    curr.pop()
                node = node.children[val]
        util(0, self.root)
        return res

                
                

            

        