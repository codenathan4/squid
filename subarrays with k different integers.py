class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def findAtMostK(nums,d):
            rec = defaultdict(int);
            ans=s=ct=0
            for i in range(len(nums)):
                if rec[nums[i]]==0:
                    rec[nums[i]] += 1
                    ct += 1
                while ct > d:                
                    if rec[nums[s]] - 1 == 1:
                        rec[nums[i]] -= 1
                        s += 1
                        ct -= 1
              
                ans += i-s
          
            return ans
        
        return findAtMostK(nums,k) - findAtMostK(nums,k-1)
