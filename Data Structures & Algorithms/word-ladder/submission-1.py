class Solution:
    def __init__(self):
        self.wordMap = defaultdict(set)

    def createWordMap(self, word):
        for i in range(len(word)):
            currHash = word[:i] + "*" + word[i+1:]
            self.wordMap[currHash].add(word)

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = [beginWord] + wordList
        for word in wordList:
            self.createWordMap(word)
        q = collections.deque()
        q.append((beginWord, 1))
        visited = set()
        while q:
            word, t = q.popleft()
            if word == endWord:
                return t
            if word in visited:
                continue
            visited.add(word)
            for i in range(len(word)):
                currHash = word[:i] + "*" + word[i+1:]
                for neigh in self.wordMap[currHash]:
                    if neigh not in visited:
                        q.append((neigh, t + 1))
        return 0
            

                

                







        
        