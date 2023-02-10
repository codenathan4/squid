class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        start=[]
        end=[]
        count = 0
        for i in nums:
            if target.startswith(i):
                start.append(target[len(i):])
            else:
                start.append(0)
            if target.endswith(i):
                end.append(target[:-len(i)])
            else:
                end.append(0)
                
        for i in range(len(nums)):
            for j in range(len(start)):
                if nums[i] == start[j] and i!=j:
                    count += 1
                
            for j in range(len(end)):
                if nums[i] == end[j] and i!=j:
                    count += 1
                
        print(start,end)        
        return count//2 
