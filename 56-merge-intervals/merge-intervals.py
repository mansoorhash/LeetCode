class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        left, right = intervals[0]
        result = []
        for interval in intervals[1:]:
            l, r = interval
            
            if l <= right:
                right = max(right, r)
            else:
                result.append([left,right])
                left,right = l, r
        result.append([left,right])

        return result
                

        