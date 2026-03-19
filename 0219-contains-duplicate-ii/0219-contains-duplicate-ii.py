class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #using sliding window
        # 1,2,3 (k=3) ,,,1,2,3,4(k=4)
        seen = set()

        # nums = [1,2,3,1]
        # nums = [1,2,3,4,1]
        #k=3
        for idx, num in enumerate(nums):
            if num in seen:
                return True
            seen.add(num)
            #k=3 , len(seen) = 4
            if len(seen) > k:
                seen.remove(nums[idx-k])
        return False
        