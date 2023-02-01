class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        h = sorted(zip(growTime,plantTime),reverse=True)
        out = 0
        temp = 0
        
        for i in h:
            temp += i[1]
            if temp+i[0] > out:
                out = temp+i[0]
                
        return out 
