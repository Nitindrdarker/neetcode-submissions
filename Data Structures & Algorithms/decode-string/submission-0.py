class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i == ']':
                string = ''
                integerString = ''
                while stack and stack[-1] != '[':
                    string = stack.pop() + string
                stack.pop()
                while stack and stack[-1].isnumeric():
                    integerString = stack.pop() + integerString
                val = string * int(integerString)
                stack.append(val)
            else:
                stack.append(i)
        return ''.join(stack)

                    