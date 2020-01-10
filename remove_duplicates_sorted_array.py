class Solution:
    def removeDuplicates(self, nums) :
        n=len(nums)
        if n==0 or n==1 :
            return n
        i=1
        while True :
            if nums[i]==nums[i-1] :
                nums.pop(i)
                i-=1
            i+=1
            if i==len(nums) :
                break
        return len(nums)