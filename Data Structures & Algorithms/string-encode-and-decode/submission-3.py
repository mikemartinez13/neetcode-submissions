class Solution:

    def encode(self, strs: List[str]) -> str:
        out = []
        for s in strs: 
            out.append(str(len(s))+'-')
            out.append(s)
        print(out)
        return "".join(out)
    def decode(self, s: str) -> List[str]:
        
        i = 0
        final = []
        while i < len(s):
            init_length = ""
            while s[i]!= '-':
                init_length += s[i]
                i+=1
            init_length = int(init_length)    
            
            i+=1
            new = ""
            while len(new) < init_length:
                new += s[i]
                i+=1
            final.append(new)

        return final
        
