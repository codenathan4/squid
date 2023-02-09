class Solution:
    def reformatDate(self, date: str) -> str:
        d = {"Jan":'01',"Feb":'02',"Mar":'03',"Apr":'04',"May":'05',"Jun":'06', "Jul":'07',"Aug":'08',"Sep":'09',"Oct":'10',"Nov":'11',"Dec":'12'}
        if len(date) == 13:
            return '-'.join([date[9:13],d[date[5:8]],date[:2]])
        if len(date) == 12:
            return '-'.join([date[8:12],d[date[4:7]],'0'+date[:1]]) 
