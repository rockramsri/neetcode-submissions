class Solution:
    def longestPalindrome(self, s: str) -> str:
        for i in range(0,len(s)):
            w_s=len(s)-i
            for j in range(0,len(s)):
                #print(j,j+w_s)
                if j+w_s>len(s):
                    break
                w_str=s[j:j+w_s]
                #print(w_str)
                if w_str == w_str[::-1]:
                    return w_str
        return ""