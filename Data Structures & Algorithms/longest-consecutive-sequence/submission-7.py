class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=sorted(list(set(nums)))
        #print(s)
        m=0
        long=1
        maxLong=0
        #print(s,max(s))
        if len(s)==0:
            return 0
        #print(s)
        for i in range(0,len(s)-1):
            if s[i]+1 == s[i+1]:
                long+=1
            else:
                maxLong=max(maxLong,long)
                long=1
            #print(long)
        return max(maxLong,long)
            
            