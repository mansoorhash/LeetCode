class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        p = 1
        for i in range(len(digits)-1, -1 , -1):
            v = digits[i] + p
            p = v // 10
            digits[i] = v % 10
        if p:
            digits.insert(0, p)
        return digits

        
        