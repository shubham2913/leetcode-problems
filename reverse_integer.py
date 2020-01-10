class Solution:
    def reverse(self, x) :
        s=str(x)
        if x < 0 :
            s=s[1:]
        l=[]
        for si in s :
            l.append(si)
        l.reverse()
        srev=""
        for i in l :
            srev+=i
        xrev=int(srev)
        if x < 0 :
            xrev*=-1
        if xrev not in range(-2**31,2**31) :
            return 0
        else :
            return xrev