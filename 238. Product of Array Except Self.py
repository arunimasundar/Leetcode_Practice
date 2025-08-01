#238. Product of Array Except Self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        #First approach using two arrays to store the product of elements before and after each index
        # parr=[1]*len(nums)
        # sarr=[1]*len(nums)

        # i=1
        # j=len(nums)-2
        # while i<len(nums) and j>=0:
        #     parr[i]=parr[i-1]*nums[i-1]
        #     i+=1
        #     sarr[j]=sarr[j+1]*nums[j+1]
        #     j-=1
        
        # ans=[]
        # for i in range(0,len(nums)):
        #     ans.append(parr[i]*sarr[i])
        # return ans
        
        #Second approach using constant space
        ans=[1]*len(nums)
        p=1
        for i in range(len(nums)):
            ans[i]=p
            p=p*nums[i]
        
        suff=1

        for i in reversed(range(len(nums))):
            ans[i]=ans[i]*suff
            suff=suff*nums[i]
        return ans



