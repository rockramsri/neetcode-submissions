class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat=[]
        for i in matrix:
            flat.extend(i)
        print(flat)
        if target in flat:
            return True
        # mid=len(flat)//2
        # lower=0
        # upper=len(flat)-1
        # while lower<upper

        # for i in range(0,len(matrix)):
        #     for j in range()
        return False