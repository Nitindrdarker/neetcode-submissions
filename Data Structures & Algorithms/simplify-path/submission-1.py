class Solution:
    def simplifyPath(self, path: str) -> str:
        s = path.split("/")
        stack = []
        for i in s:
            if i == '' or i == '.':
                continue
            elif i == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        return '/' + '/'.join(stack)