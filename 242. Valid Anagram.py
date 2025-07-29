#242. Valid Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        sdict={}
        for char in s:
            if char not in sdict:
                sdict[char]=1
            else:
                sdict[char]+=1
        
        tdict={}
        for char in t:
            if char not in tdict:
                tdict[char]=1
            else:
                tdict[char]+=1

        if sdict==tdict:
            return True
        else:
            return False
        
