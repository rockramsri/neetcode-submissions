class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result=[[]]
        current_path=[]
        def subseter(current_path,choices):
            # if len(choices)==0:
            #     print(current_path)
            #     self.result.append(current_path.copy())
            #     print(self.result)
            #     return
            for i in range(0,len(choices)):
                current_choice=choices[i]
                current_path.append(current_choice)
                self.result.append(current_path.copy())
                rem_choice=choices[i+1:]
                subseter(current_path,rem_choice)
                current_path.pop()
        print(subseter(current_path,nums))
        print(self.result)
        return self.result