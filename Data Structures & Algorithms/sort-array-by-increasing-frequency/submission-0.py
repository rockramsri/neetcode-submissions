class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        m=[]
        frq=[]
        for i in nums:
            if i not in m:
                m.append(i)
                frq.append(1)
            else:
                frq[m.index(i)]+=1
        print(m,frq)
        for i in range(0,len(m)):
            for j in range(i,len(m)):
                if frq[i]>frq[j] or (frq[i]==frq[j] and m[i]<m[j]):
                    frq[i],frq[j]=frq[j],frq[i]
                    m[i],m[j]=m[j],m[i]
        rest=[]
        print(m,frq)
        for i in range(0,len(m)):
            rest+=([m[i]]*frq[i])
        return rest



        