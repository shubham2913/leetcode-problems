class Solution:
    def intToRoman(self, num) :
        s=""
        d=[(1,'I'),(4,'IV'),(5,'V'),(9,'IX'),(10,'X'),(40,'XL'),(50,'L'),(90,'XC'),(100,'C'),(400,'CD'),(500,'D'),(900,'CM'),(1000,'M')]
        l=len(d)
        while num > 0 :
            for i in range(l-1,-1,-1) :
                if num>=d[i][0] :
                    s+=d[i][1]
                    num-=d[i][0]
                    break
        return s