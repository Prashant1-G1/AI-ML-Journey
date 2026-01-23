class Solution(object):
    def removeElement(self, nums, val):
        k=0
        for x in range(len(nums)):
            if nums[x]!=val:
                nums[k]=nums[x]
                k+=1

        return k
    
sl=Solution()
nums=[1,1,1,2,2,3,3]
print(sl.removeElement(nums,2))