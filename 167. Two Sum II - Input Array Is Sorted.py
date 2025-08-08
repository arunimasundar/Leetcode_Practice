# 167. Two Sum II - Input Array Is Sorted

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # dict method
        # numdict={}
        # for i in range(len(numbers)):
        #     k=target-numbers[i]
        #     if numbers[i] not in numdict:
        #         numdict[k]=i+1
        #     else:
        #         return[numdict[numbers[i]],i+1]
        
        # two pointers method

        l=0
        r=len(numbers)-1
        while l<r:
            s = numbers[l] + numbers[r]
            if(s==target):
                return[l+1,r+1]
            elif s<target:
                l+=1
            else:
                r-=1


        