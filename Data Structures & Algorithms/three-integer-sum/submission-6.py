from collections import Counter
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ct=Counter(nums)
        m=sorted(ct.keys())
        result=set()
        if 0 in ct.keys() and ct[0]>2:
            result.add((0,0,0))
        for i in range(0,len(m)):
            for j in range(i+1,len(m)):
                #print([m[i],m[j],-(m[i]+m[j])])
                if -(m[i]+m[j]) in ct.keys() and ( len(Counter([m[i],m[j],-(m[i]+m[j])])-ct)==0 ):
                    result.add(tuple(sorted([m[i],m[j],-(m[i]+m[j])])))
                    # ct[m[i]]-=1
                    # ct[m[j]]-=1
                    # ct[-(m[i]+m[j])]-=1
        return [list(row) for row in result]

        
        