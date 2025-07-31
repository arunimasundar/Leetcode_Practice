#Encode and Decode Strings

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=""
        for s in strs:
            encoded+=str(len(s))+'#'+s
        print(encoded)
        return encoded


    def decode(self, s: str) -> List[str]:

        decoded = []
        i=0
        while i<len(s):
            j=i
            while(s[j]!='#'):
                j+=1
            l=int(s[i:j])
            i=j+1
            j=i+l
            decoded.append(s[i:j])
            i=j


        
        return decoded
