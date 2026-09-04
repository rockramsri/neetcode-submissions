class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [4,5,6,7,2,3]
        # [   ]
        if len(nums)==1:
            return nums[0]
        if nums[0]<nums[len(nums)-1]:
            return nums[0]
        l=0
        r=len(nums)-1
        me=nums[0]
        while l<r:
            mid=(l+r)//2
            if nums[mid]>nums[r]:
                # mid is in the right segment
                l=mid+1
            else:
                r=mid
            me=min(nums[mid],me)
        return nums[l]
            
        
        
        