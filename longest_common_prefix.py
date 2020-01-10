class Solution:
    def longestCommonPrefix(self, strs) :
        strings=[(s,len(s)) for s in strs]
        strings.sort(key=lambda x : x[1])
        if len(strings)==0 :
            return ""
        s1=strings[0][0]
        i = len(s1)
        while i >=1 :
            count=0
            for s,l in strings :
                if s[:i]==s1[:i]  :
                    count+=1
            if count==len(strings) :
                return s1[:i]
            i-=1
        return ""