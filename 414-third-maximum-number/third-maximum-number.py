class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        ranking = {
            "first": float('-inf'),
            "second": float('-inf'),
            "third": float('-inf'),
        }

        for n in nums:
            if ranking["first"] < n:
                ranking["third"], ranking["second"] = ranking["second"], ranking["first"]
                ranking["first"] = n
            elif ranking["second"] < n:
                ranking["third"] = ranking["second"]
                ranking["second"] = n
            elif ranking["third"] < n:
                ranking["third"] = n
        return ranking["first"] if ranking["third"] == float('-inf') else ranking["third"]
