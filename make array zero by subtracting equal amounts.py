class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        m = nums[len(nums)-1]
        c = 0
                
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]:
                print(m)
                m = m + nums[i-1] - nums[i]
                print(m)
                c += 1
            if m <= 0:
                return c
        
        
        if nums[0] == 0: return 0
        return c+1
