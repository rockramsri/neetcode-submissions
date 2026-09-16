from collections import Counter
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result=set()
        #ct={}
        # def trie(copy_path):
        #     if 
        def depth(path,nr):
            for i in range(len(nr)):
                current_nr=nr[i]
                result.add(tuple(path+[current_nr]))
                rem_nr=nr[i+1:]
                depth(path+[current_nr],rem_nr)
            pass
        depth([],sorted(nums))
        return [list(i) for i in result]+[[]]