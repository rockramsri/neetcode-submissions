class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=""
        for i in s:
            if i.isalnum():
                st+=i

        return True if st.lower() == st[::-1].lower() else False
        