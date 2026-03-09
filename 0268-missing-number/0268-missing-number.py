class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # nums.sort()
        # cnt = 0
        # for i in range(len(nums)):
        #     if nums[i] != cnt :
        #         return(i)
        #     cnt += 1
        # return(cnt)
        
        nums.sort()

        for i,v in enumerate(nums):
            if (i != v):
                return v-1
            
            if v == len(nums)-1:
                return v+1