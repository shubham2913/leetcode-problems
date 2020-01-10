class Solution:
    def lengthOfLongestSubstring(self, s):
        n=len(s)
        if n==0 :
            return 0
        max_length=[1 for i in range(n)]
        i=1
        while i < n :
            l=1
            for j in range(i-max_length[i-1],i) :
                if s[j]==s[i] :
                    l=1
                else :
                    l+=1
            max_length[i]=l
            i+=1
        return max(max_length)