class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # condition of the ireations
        # consition foth trmeinations
        # problem : () 
        result=[]
        

        def backtrack(path,open_count,close_count):
            if len(path) == 2*n:
                result.append(path)
                return
            if open_count<n:
                backtrack(path+"(",open_count+1,close_count)
            if close_count<open_count:
                backtrack(path+")",open_count,close_count+1)
            pass
        backtrack("",0,0)
        print(result)
        return result