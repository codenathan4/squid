class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        rec=defaultdict(int)
        count = 0
        n=len(nums)
        prfx=0
        rec[0]+=1
        
        for i in range(n):
            prfx += nums[i]
            count += rec[prfx%k]
            rec[prfx%k]+=1
            
        return count
