class Solution:
    def countSubstrings(self, s: str) -> int:
        self.count=0
        def expandFromCenter(left,right):
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
                self.count+=1
            return
        for i in range(len(s)):
            expandFromCenter(i,i)
            expandFromCenter(i,i+1)
        print(self.count)
        return self.count

        