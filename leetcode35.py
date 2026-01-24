class Solution(object):
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        else:
            for x in range(len(nums)):
                if target<nums[x]:
                    return x
        
        if target>nums[len(nums)-1]:
            return len(nums)
        