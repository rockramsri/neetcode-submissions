class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # to fidn the cutindex for the 2 sorted arry
        #[3,4,5,6,1,2]
        # if len(nums)==1:
        #     if nums[0]==target:
        #         return 0
        #     else:
        #         return -1
        l,r=0,len(nums)-1
        while l<r:
            mid=(l+r)//2
            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid
        print(l,r)
        if nums[0]<=target:
            if l==0:
                l,r=0,len(nums)-1
            else:
                r,l=l-1,0
            while l<=r:
                mid=(l+r)//2
                if nums[mid]==target:
                    return mid
                if nums[mid]>target:
                    r=mid-1
                else:
                    l=mid+1
        else:
            r=len(nums)-1
            print(l,r)
            while l<=r:
                mid=(l+r)//2
                if nums[mid]==target:
                    return mid
                if nums[mid]>target:
                    r=mid-1
                else:
                    l=mid+1
        
        return -1

        # lsegment=False
        # if nums[r]>target:
        #     lsegment=True
        # while l<r:
        #     mid=(l+r)//2
        #     if lsegment:
        #         if nums[mid]==target:
        #             return mid
        #         elif nums[mid]>target:
        #             r=mid-1
        #         else:
        
                

        