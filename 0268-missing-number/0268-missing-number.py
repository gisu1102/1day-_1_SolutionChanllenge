class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # nums.sort()
        # cnt = 0
        # for i in range(len(nums)):
        #     if nums[i] != cnt :
        #         return(i)
        #     cnt += 1
        # return(cnt)
        
        # nums.sort()

        # for i,v in enumerate(nums):
        #     if (i != v):
        #         return v-1
            
        #     if v == len(nums)-1:
        #         return v+1

        # 0 1 2 (3) 
        # 3 ,6 
        # 0 1 3 
        # 4 6
        return sum(range(0, len(nums)+1)) - sum(nums)