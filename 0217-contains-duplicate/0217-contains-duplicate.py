class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        sorted_num = sorted(nums)
        for i in range(1,len(sorted_num)):
            if sorted_num[i] == sorted_num[i-1]:
                return True
        return False
        # if len(set(nums)) == len(nums):
        #     return False
        # else :
        #     return True
        