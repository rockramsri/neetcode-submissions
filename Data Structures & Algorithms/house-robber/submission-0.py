class Solution:
    def rob(self, nums: List[int]) -> int:
        mat=[0 for _ in range(len(nums))]
        mat[0]=nums[0]
        if len(nums)>1:
            mat[1]=max(nums[:2])
        for i in range(2,len(nums)):
            mat[i]=max(mat[i-1],nums[i]+mat[i-2])
        return mat[-1]
        