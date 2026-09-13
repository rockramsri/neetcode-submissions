class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        def recur(c_path,r_c,t,c_s):
            for i in range(len(r_c)):
                if c_s+r_c[i] > t or (i>0 and r_c[i]==r_c[i-1]):
                    continue
                elif c_s+r_c[i] == t:
                    #result.add(frozenset(c_path.copy()+[r_c[i]]))
                    result.append(c_path.copy()+[r_c[i]])
                    break
                current_lock=r_c[i]
                c_path.append(current_lock)
                recur(c_path,r_c[i+1:],t,c_s+current_lock)
                c_path.pop()
            #print(result,c_path,r_c,t,c_s)
            pass
        current_path=[]
        candidates.sort()
        remaining_cand=candidates
        recur(current_path,remaining_cand,target,0)
        print(result)
        return result #[list(i) for i in result]
        