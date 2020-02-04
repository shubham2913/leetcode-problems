class Solution:
    def isPalindrome(self, x) :
        s=str(x)
        l=len(s)
        if l==0 :
            return False
        if l==1 :
            return True
        if s[0]=='-' :
            return False
        for i in range(int(l/2)) :
            if s[i]!=s[l-i-1] :
                return False
        return True