# 347. Top K Frequent Elements

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter=Counter(nums)
        counter_desc = sorted(counter.items(),key=lambda item:item[1], reverse = True)
        l = [tup[0] for tup in counter_desc]
        return l[0:k]
        