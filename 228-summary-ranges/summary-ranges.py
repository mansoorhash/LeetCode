class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        start = ""
        end = ""
        res = []
        i = 0
        while i < len(nums):
            number = nums[i]
            if not start: start = str(number)
            
            if (i+1 < len(nums)) and nums[i+1] == number+1:
                end = str(nums[i+1])
            else:
                if not end:
                    res.append(start)
                else: 
                    res.append(start + "->" + end)
                start = ""
                end = ""

            i+=1 
        return res