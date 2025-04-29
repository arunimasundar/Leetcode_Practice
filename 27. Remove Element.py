# 27. Remove Element

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]
                k+=1
        return k

# The time complexity of this solution is O(n), where n is the length of the input list nums. This is because we are iterating through the list once to check each element.