class Solution:
    def romanToInt(self, s) :
        d1={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        d2={}
        for k1 in d1 :
            d2[k1]=d1[k1]
            for k2 in d1 :
                if d1[k1] < d1[k2] :
                    d2[k1+k2]=d1[k2]-d1[k1]
                else :
                    d2[k1+k2]=d1[k2]+d1[k1]
        l=len(s)
        i=l-1
        ans=0
        while i>=0 :
            if i==0 :
                print(d2[s[i]])
                ans+=d1[s[i]]
            else :
                if d1[s[i]] > d1[s[i-1]] :
                    ans+=-d1[s[i-1]]+d1[s[i]]
                    i-=1
                else :
                    ans+=d1[s[i]]
            i-=1
        return ans