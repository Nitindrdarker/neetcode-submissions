class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            if digits[i] + 1 > 9:
                digits[i] = 0
                carry = 1
            else:
                digits[i] += 1
                return digits
            
        if carry == 1:
            return [carry] + digits
        return digits