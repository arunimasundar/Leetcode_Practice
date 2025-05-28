#80. Remove Duplicates from Sorted Array II

from collections  import Counter
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        all_counts = dict()
        k=0
        for i in range(0,len(nums)):
            if nums[i] not in all_counts:
                all_counts[nums[i]]=1
                nums[k]=nums[i]
                k+=1
                
            else:
                all_counts[nums[i]]+=1
                if(all_counts[nums[i]]<=2):
                    nums[k]=nums[i]
                    k+=1

        return k


        