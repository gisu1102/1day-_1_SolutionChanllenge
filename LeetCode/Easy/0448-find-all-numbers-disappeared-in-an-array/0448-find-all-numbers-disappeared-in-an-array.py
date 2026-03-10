class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        # set
        #[4,3,2,7,8,1]
        set_nums = set(nums)
        ans = []
        #len(nums)+1
        # idx <-> num 
        for i in range(1,len(nums)+1):
            if i not in set_nums:
                ans.append(i)
        
        return ans