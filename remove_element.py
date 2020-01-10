class Solution:
    def removeElement(self, nums, val):                     
        if len(nums)==0 :
            return 0
        i=0
        while True :
            if nums[i]==val :
                nums.pop(i)
                i-=1
            i+=1
            if i==len(nums) :
                break
        return len(nums)