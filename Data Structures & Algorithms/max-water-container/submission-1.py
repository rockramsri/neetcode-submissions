class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # maxArea=0
        # for i in range(len(heights)):
        #     for j in range(len(heights)-1,i,-1):
        #         #print(i,j)
        #         tempMax=min(heights[i],heights[j])*abs(j-i)
        #         maxArea=max(tempMax,maxArea)
        # return maxArea
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
        # while (i>=0 or j<len(heights)):
        #     if i-1>=0 and j+1<len(heights):
        #         newArea2=abs(j-i+2)*min(heights[i-1],heights[j+1])
        #     if i-1>=0:
        #         newAreaL=abs(j-i+1)*min(heights[i-1],heights[j])
        #     if j+1<len(heights):
        #         newAreaR=abs(j-i+1)*min(heights[i],heights[j+1])
        #     maxArea=max(newArea2,newAreaL,newAreaR,maxArea)
        #     j+=1
        #     i-=1
        #     #print(i,j,maxArea)
        # print(maxArea)
        #return maxArea
            
            

            

        

        