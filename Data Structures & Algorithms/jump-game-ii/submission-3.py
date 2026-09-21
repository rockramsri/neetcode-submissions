class Solution:
    def jump(self, nums: List[int]) -> int:
        jp=[ i+nums[i] for i in range(len(nums)) ]
        print(jp)
        i=0
        step=0
        m=nums[0]
        if len(nums)==1:
            return 0
        while True:
            if m>=len(nums)-1:
                break
            for k in range(i+1,jp[i]+1):
                # if jp[i]>=len(nums):
                #     break
                if jp[k]>m:
                    m=jp[k]
                    i=k
            step+=1
            
            print(m,i)
        return step+1


        