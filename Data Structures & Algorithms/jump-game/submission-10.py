class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums[0]==0 and len(nums)!=1:
            return False
        i=0
        m_j=[i+nums[i] for i in range(0,len(nums))]
        print(m_j)
        rt=nums[i]
        while True:
            # Save the old reach before calculating the new one
            prev_rt = rt 
            
            rt = max(m_j[i:rt+1])
            
            if rt >= len(nums)-1:
                return True
                
            # If our max reach didn't increase, we are stuck
            if rt == prev_rt: 
                return False
                
            # Advance 'i' only to the end of the previous window
            i = prev_rt

        return False
        