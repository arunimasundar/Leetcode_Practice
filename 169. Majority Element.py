from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        dict1 = dict(Counter(nums))
        dict1 = dict(sorted(dict1.items(), key=lambda item: item[1], reverse=True))
        
        return next(iter(dict1))
        