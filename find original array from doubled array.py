class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)%2!=0:
            return []
        changed.sort()
        temp=[]
        orignal=[]
        for i in changed:
            if not temp:
                orignal.append(i)
                temp.append(i)
                continue
            if i==2*temp[0]:
                temp.pop(0)
                continue
            orignal.append(i)
            temp.append(i)
        print(orignal,temp)
        return orignal if not temp else []
