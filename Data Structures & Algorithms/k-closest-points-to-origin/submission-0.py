import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        m=heapq.nsmallest(k,points,key=lambda x:(x[1]**2 + x[0]**2)**(1/2))
        #print(m)
        return m
        