class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        # nested Loop Solution

        #8 1 2 2 3
        sorted_nums = sorted(nums) #1 2 2 3 8
        d ={} # {1:0, 2:1, 3:3, 8:4}

        for idx, num in enumerate(sorted_nums):
            if num not in d:
                d[num] = idx
        
        ret = []

        for num in nums:
            ret.append(d[num])
        
        return ret

