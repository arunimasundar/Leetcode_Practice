# 128. Longest Consecutive Sequence


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        st=set()
        longest = 0
        for n in nums:
            st.add(n)
        for n in nums:
            if n in st and n-1 not in st :
                cur = n
                c=0
                while cur in st:
                    st.remove(cur)
                    cur+=1
                    c+=1
                longest = max(longest,c)
        return longest



