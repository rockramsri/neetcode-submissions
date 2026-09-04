class Solution:
    def maxArea(self, heights: List[int]) -> int:
        sHeights=sorted(heights,reverse=True)
        larPos=heights.index(sHeights[0])
        lar2Pos=len(heights)-1 - heights[::-1].index(sHeights[1])
        i,j=min(larPos,lar2Pos),max(larPos,lar2Pos)
        maxArea=sHeights[1]*abs(j-i)
        print(maxArea,i,j)
        for point in range(j,len(heights)):
            tempArea=abs(point-i)*min(heights[i],heights[point])
            if tempArea>=maxArea:
                j=point
                maxArea=tempArea
        for point in range(i,-1,-1):
            tempArea=abs(point-j)*min(heights[j],heights[point])
            if tempArea>=maxArea:
                i=point
                maxArea=tempArea
        return maxArea
            
            

            

        

        