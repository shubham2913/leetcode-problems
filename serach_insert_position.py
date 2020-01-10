class Solution:
    def searchInsert(self, nums, target):
        s=0;
        e=len(nums)-1
        while(s<=e) :
            c=s+int((-s+e)/2)
            if nums[c]==target :
                return c
            else :
                if nums[c] > target :
                    e=c-1
                else :
                    s=c+1
        return s