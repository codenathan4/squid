class Solution:
    def _3digit(self, num):
        if num == 0:
            return ''
        elif num < 20:
            return self.A[num] + ' '
        elif num < 100:
            return self.B[num // 10] + ' ' + self._3digit(num % 10)
        else:
            return self.A[num // 100] + ' Hundred ' + self._3digit(num % 100)

    def numberToWords(self, num: int) -> str:
        
        if num == 0:
            return 'Zero'

        out = ''
        for i, _3 in enumerate(self.C):
            if num % 1000 != 0:
                out = self._3digit(num % 1000) + _3 + ' ' + out
            num //= 1000
        return out.strip()
        
        
        
        
        
        
        
        
        
        
        
    A = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    B = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    C = ["", "Thousand", "Million", "Billion"];
        
