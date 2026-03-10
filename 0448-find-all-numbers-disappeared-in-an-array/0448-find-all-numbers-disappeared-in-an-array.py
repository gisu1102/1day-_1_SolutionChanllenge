class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        # # set
        # #[4,3,2,7,8,1]
        # set_nums = set(nums)
        # ans = []

        # #len(nums)+1
        # # idx <-> num 
        # for i in range(1,len(nums)+1):
        #     if i not in set_nums:
        #         ans.append(i)
        
        # return ans

        for num in nums:
            idx = abs(num) -1
            if nums[idx] > 0:
                nums[idx] *= -1
        
        res = []
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i+1)
        
        return res
