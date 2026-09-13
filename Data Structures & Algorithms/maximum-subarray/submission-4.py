class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx=float('-inf')
        cs=0
        for num in nums:
            cs+=num
            mx=max(cs,mx)
            if cs<0:
                cs=0
        return mx


