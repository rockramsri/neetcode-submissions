class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def recur(r_c,c_p):
            for i in range(len(r_c)):
                current_lock=r_c[i]
                recur(r_c[:i]+r_c[i+1:],c_p+[current_lock])
                if len(c_p)+1 == len(nums):
                    result.append(c_p+[current_lock])
            pass
        current_path=[]
        recur(nums.copy(),current_path)
        #print(result)
        return result