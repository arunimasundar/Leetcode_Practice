# 11. Container With Most Water


class Solution:
    def maxArea(self, height: List[int]) -> int:

        l=0
        r=len(height)-1
        arr=0
        while l<r:
            row=(r-l)
            temp=row*min(height[l],height[r])
            if temp>arr:
                arr=temp
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return arr

