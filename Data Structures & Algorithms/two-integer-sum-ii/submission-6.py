class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r=set()
        r.add(numbers[0])
        for i in range(1,len(numbers)):
            if (target-numbers[i]) in r:
                return [numbers.index( (target-numbers[i]) )+1,i+1]
            else:
                r.add(numbers[i])


        