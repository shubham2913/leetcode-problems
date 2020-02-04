class Solution:
    def convert(self, s, numRows):
        i=0
        l=len(s)
        if l==0 or l==1:
            return s
        if numRows==1 :
            return s
        flag=-1
        p=[(s[0],1)]
        for j in range(1,l) :
            if i==0 :
                flag=1
                i+=2
            elif i==(numRows+1) :
                flag=-1
                i-=2
            p.append((s[j],i))
            i+=flag
        k=1
        ans=""
        while(k<=numRows) :
            for c in p :
                if c[1]==k :
                    ans+=c[0]
            k+=1
        return ans