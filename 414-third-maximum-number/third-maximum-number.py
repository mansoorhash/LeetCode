class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = float('-inf')
        second = float('-inf')
        third = float('-inf')

        for n in nums:
            if n == first or n == second or n == third:
                continue
            elif first < n:
                third, second = second, first
                first = n
            elif second < n:
                third = second
                second= n
            elif third < n:
                third = n
        return first if third== float('-inf') else third
