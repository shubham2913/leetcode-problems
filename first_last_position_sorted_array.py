class Solution:
    def searchRange(self, nums, target) :
        s = 0;
        e = len(nums) - 1
        index=-1
        while (s <= e):
            c = s + int((e - s) / 2)
            if nums[c] == target:
                index=c
                break
            else:
                if nums[c] > target:
                    e = c - 1
                else:
                    s = c + 1
        if index==-1 :
            return [-1,-1]
        else :
            n=len(nums)
            i=index+1
            ei=index
            while(i<n) :
                if nums[i]!=nums[index] :
                    break
                else :
                    ei=i
                i=i+1
            si=index
            j=index-1
            while(j>=0) :
                if nums[j]!=nums[index] :
                    break
                else :
                    si=j
                j=j-1
        return [si,ei]