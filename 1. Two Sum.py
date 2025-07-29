#1. Two sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
     
        vdict = {}
        for i in range(0,len(nums)):
            val = target-nums[i]
            if(val in vdict):
                return [i,vdict[val]]
            else:
                vdict[nums[i]]=i
        return []

