class Solution:
    def isPalindrome(self, s: str) -> bool:
        ms = ""

        for i in range(len(s)):
            if s[i].isalnum():
                ms += s[i].lower()
        
        left = 0
        right = len(ms)-1

        while left < right:
            #print("checking left:", ms[left],"vs right:",ms[right])
            if ms[left]!=ms[right]:
                return False
            left +=1
            right -=1
        
        return True