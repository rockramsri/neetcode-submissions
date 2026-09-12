from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return len(Counter(s)-Counter(t))==0 and len(Counter(t)-Counter(s))==0