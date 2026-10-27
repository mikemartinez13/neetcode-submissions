class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        for i in range(len(s)):
            s_val = s_dict.get(s[i],0)+1
            s_dict[s[i]] = s_val
        for j in range(len(t)):
            t_val = t_dict.get(t[j],0)+1
            t_dict[t[j]] = t_val
        
        if s_dict == t_dict: 
            return True

        return False