class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        tens = 0
        fives = 0
        for i in bills:
            
            if i == 20:
                if tens >= 1 and fives >= 1:
                    tens -= 1
                    fives -= 1
                elif fives >= 3:
                    fives -= 3
                else:
                    return False
            elif i == 10:
                if fives:
                    fives -= 1
                    tens += 1
                else:
                    return False
            else:
                fives += 1
        return True
