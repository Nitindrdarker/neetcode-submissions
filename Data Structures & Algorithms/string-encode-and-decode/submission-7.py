class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for word in strs:
            res.append(str(len(word)) + "#" + word)
        print(res)
        return ''.join(res)


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            length = 0
            while i < len(s) and s[i] != '#':
                length = length * 10 + int(s[i])
                i += 1
            i += 1
            res.append(s[i:length + i])
            i = length + i
        return res



