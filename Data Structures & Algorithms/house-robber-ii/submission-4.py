class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=3:
            return max(nums)
        m=[0 for i in range(len(nums)-1)]
        m1=[0 for i in range(len(nums)-1)]
        m[0] = nums[0]
        m[1] = max(m[0],nums[1])
        for i in range(2,len(nums)-1):
            m[i] = max( m[i-1] , nums[i] + m[i-2] )
        nums=nums[1:]
        m1[0] = nums[0]
        m1[1] = max(m1[0],nums[1])
        for i in range(2,len(nums)):
            m1[i] = max( m1[i-1] , nums[i] + m1[i-2] )
        #max( cost(i-1 ), cost(i + i-2) ) , if max( cost (last_element - n[0] if n[0] is in the path) + cost(n-1) )
        return max(m[-1],m1[-1])
        