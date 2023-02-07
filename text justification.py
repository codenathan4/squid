class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        d = maxWidth
        i = 0
        s = 0
        out = []
        
        while i < len(words): 
            if d - len(words[i]) < i - 1 -s:
                temp = ''
                if i == s + 1:
                    l=d
                    temp += words[i-1]
                    temp += ' '*d
                else:
                    l = (d)%(i-1-s)
                    for j in words[s:i-1]:
                        temp += j
                        temp += ' '*((d)//(i-1-s))
                        if l>0: temp += ' '
                        l-=1 
                    temp += words[i-1]    
                out.append(temp)        
                d = maxWidth
                s = i
            d -= len(words[i])
            i += 1
            
        print(s,out)
