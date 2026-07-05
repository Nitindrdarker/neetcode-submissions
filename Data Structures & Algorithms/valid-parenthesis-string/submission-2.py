class Solution:
    def checkValidString(self, s: str) -> bool:
        stars = []
        stack = []
        for idx, i in enumerate(s):
            if i == ')' and stack and stack[-1][1] == '(':
                stack.pop()
            elif i == '*':
                stars.append(idx)
            else:
                stack.append((idx, i))
        temp = []
        while stack:
            i, val = stack[-1]
            if val == '(' :
                if stars and i < stars[-1]:
                    stack.pop()
                    stars.pop()
                else:
                    return False
            else:
                stack.pop()
                temp.append((i, val))
        
        if not stack and not temp:
            return True
        print(temp, stars)
        i = 0
        while temp:
            idx, v = temp[-1]
            if v == ')':
                if i < len(stars) and stars[i] < idx:
                    i += 1
                    temp.pop()
                    continue
                else:
                    return False
        if not temp:
            return True
        return False


        


