class Solution:
    def minimumDeletions(self, s: str) -> int:
        a=b=c=0
        for i in s:
            if i == 'a':
                a += 1
            else:
                b += 1
            if b < a:
                c += b
                a = b = 0
        return a + c
