class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for i in strs:
            res += str(len(i)) + '#' + i
        return res

    def decode(self, s: str) -> List[str]:
        print(s)
        i = 0
        res = []
        while i < len(s):
            n = 0
            while i < len(s) and s[i] != "#":
                n = (n * 10 )+ int(s[i])
                i += 1
            i += 1
            string = s[i:i+n]
            res.append(string)
            i = i + n
        return res


