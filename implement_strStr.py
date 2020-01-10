class Solution:
    def strStr(self, haystack, needle) :
        n1=len(haystack)
        n2=len(needle)
        if n2==0 :
            return 0
        if n1==0 :
            return -1
        for i in range(n1) :
            j=i+n2
            if haystack[i:j]==needle :
                return i
        return -1