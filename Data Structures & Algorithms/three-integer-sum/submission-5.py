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

        # neg=[]
        # pos=[]
        # for i in nums:
        #     if i>=0:
        #         pos.append(i)
        #     else:
        #         neg.append(i)
        # pos.sort()
        # neg.sort()
        # sp=set(pos)
        # np=set(neg)
        # result=[]
        # while len(pos)>1:
        #     if -(pos[0]+pos[1]) in sp or -(pos[0]+pos[1]) in np:
        #         result.append([pos[0],pos[1],-(pos[0]+pos[1])])
        #         neg.remove(-(pos[0]+pos[1]))
        #         pos=pos[2:]
                
        # while len(neg)>1:
        #     if -(neg[0]+neg[1]) in sp or -(neg[0]+neg[1]) in np:
        #         result.append([neg[0],neg[1],-(neg[0]+neg[1])])
        #         pos.remove(-(neg[0]+neg[1]))
        #         neg=neg[2:]
                
        # print(result,pos,neg)
        return []
        
        