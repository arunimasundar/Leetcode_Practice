# 49. Group Anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans={}
        for s in strs:
            temp = list(s)
            temp.sort()
            temp=tuple(temp)
            if temp in ans:
                ans[temp].append(s)
                
            else:
               ans[temp]=[s]

        return list(ans.values()) 

  