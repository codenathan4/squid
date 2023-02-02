class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit=[]
        letter=[]
        for i in logs:
            if i[-1].isdigit():
                digit.append(i)
            else:
                letter.append(i)
        letter.sort(key=lambda x:(x.split(" ")[1:],x.split(" ",1)))        
        return letter+digit 
