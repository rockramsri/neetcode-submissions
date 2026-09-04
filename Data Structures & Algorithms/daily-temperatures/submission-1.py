class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        revTemp=temperatures[::-1]
        finalArr=[0]
        intial=revTemp[0]
        intialIndex=0
        for i in range(1,len(revTemp)):
            if revTemp[i]>=intial:
                intial=revTemp[i]
                finalArr.append(0)
                intialIndex=i
            else:
                count=0
                for j in range(i-1,intialIndex-1,-1):
                    if revTemp[i]>=revTemp[j]:
                        count+=1
                    else:
                        break
                #print(revTemp[i],intialIndex,intial,count)
                finalArr.append(count+1)



        return finalArr[::-1]

        