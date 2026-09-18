class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            try:
                j=nums.index(target-nums[i],i+1,len(nums))
                return [i,j]
            except:
                continue
        