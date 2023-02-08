class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s=sorted(list(set(nums)))
        return s[-1] if len(s)<3 else s[-3]
