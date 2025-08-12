# 42. Trapping Rain Water

class Solution:  # 48 ms, faster than 92.74%
    def trap(self, height: List[int]) -> int:
        if(len(height)<=2):
            return 0
        n=len(height)
        maxleft=height[0]
        maxright=height[n-1]
        l=1
        r=n-2
        ans=0
        while l<=r:
            if maxleft<maxright:
                if height[l]>maxleft:
                    maxleft=height[l]
                else:
                    ans+=maxleft-height[l]
                l+=1
            else:
                if height[r]>maxright:
                    maxright=height[r]
                else:
                    ans+=maxright-height[r]
                r-=1
        return ans

