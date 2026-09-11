class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[[]]
        restar=[]
        for i in nums:
            ol=len(res)
            for j in range(ol):
                temp=res[j]+[i]
                #print(temp)
                temp_res_len=len(res)
                while sum(temp)<=target:
                    res.append(temp.copy())
                    temp.append(i)
                #print(res[len(res)-1],target)
                if len(res)!=temp_res_len and sum(res[len(res)-1])==target:
                    restar.append(res[len(res)-1])
            #print(res)
        #print(restar)
        return restar

        