# 3. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if(s==""):
            return 0
        if(len(s)==len(set(s))):
            return len(s)
        
        l=0
        r=0
        d=set()
        c=0
        maxc=0
        while l<=r<len(s):
            if s[r] not in d:
                d.add(s[r])
                r+=1
            else:
                c=r-l
                maxc=max(c,maxc)
                while s[r] in d:
                    d.remove(s[l])
                    l+=1
        return max(r-l,maxc)
       
        # arr=list(s)
        
        # l=0
        # r=1
        # c=0
        # maxc=1
        # while r<len(s):
        #     if(len(arr[l:r])==len(set(arr[l:r]))):
        #         c=len(arr[l:r])
        #         maxc=max(c,maxc)
        #         r+=1
        #     else:
        #         l+=1
        #         if l==r:
        #             r+=1
        # if(len(arr[l:])==len(set(arr[l:]))):
        #     c=len(arr[l:])
        #     maxc=max(c,maxc)

        
        # return maxc

