class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # for n in nums:
        #     count = 0
        #     for m in nums:
        #         if n == m:
        #             count += 1
        #         if count > 1 :
        #             return True
        # return False
        if len(set(nums)) == len(nums):
            return False
        else :
            return True
        