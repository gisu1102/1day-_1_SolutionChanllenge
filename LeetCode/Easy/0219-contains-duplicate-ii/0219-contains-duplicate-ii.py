class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # #using sliding window
        # # 1,2,3 (k=3) ,,,1,2,3,4(k=4)
        # seen = set()

        # # nums = [1,2,3,1]
        # # nums = [1,2,3,4,1]
        # #k=3
        # for idx, num in enumerate(nums):
        #     if num in seen:
        #         return True
        #     seen.add(num)
        #     #k=3 , len(seen) = 4
        #     if len(seen) > k:
        #         seen.remove(nums[idx-k])
        # return False

        # using Dictionary
        # 마지막 원소만 계속 갱신 
        # 만약 이전에있었으면 판단(true) or 갱신(k초과)
        last_seen = {}

        for i, num in enumerate(nums):
            if num in last_seen:
                #현재 인덱스 - 이전 인덱스 <= k
                # 0 1 2 3 4
                if i-last_seen[num] <= k:
                    return True
            last_seen[num] = i
        return False 

            

        