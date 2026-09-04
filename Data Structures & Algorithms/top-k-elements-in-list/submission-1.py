from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        coll=Counter(nums)
        result=[]
        #sorted(coll,key=lambda x:(has(x)))
        for i in coll.most_common()[:k]:
            result.append(i[0])
        return result