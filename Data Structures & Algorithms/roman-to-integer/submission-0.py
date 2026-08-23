class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {"I":1, "V": 5, "X": 10, "L":50, "C": 100, "D": 500, "M": 1000}

        stack = []
        for i in s:
            v = mapping[i]
            if stack and stack[-1] < v:
                stack.append(v - stack.pop())
            else:
                stack.append(v)
        return sum(stack)