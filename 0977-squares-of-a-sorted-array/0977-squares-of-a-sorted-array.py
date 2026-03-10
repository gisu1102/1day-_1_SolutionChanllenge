class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        # 1. sort nlogn
        # res = []
        # for num in nums:
        #     res.append(num**2)
        
        # return sorted(res)

        # # 2. merge and sort

        # #edge case
        # if not nums:
        #     return nums
        
        # if nums[0] >= 0:
        #     return [num**2 for num in nums]

        # #find index first positive = 0
        # m = len(nums)
        # for i, v in enumerate(nums):
        #     if v >= 0:
        #         m = i
        #         break

        # #A p nums
        # A = []
        # for p_num in nums[m:]:
        #     A.append(p_num**2)
        # #B n nums
        # B = []
        # for n_num in reversed(nums[:m]):
        #     B.append(n_num**2)

        # def merge(A,B):
        #     a,b = 0,0
        #     ans = []
        #     while a < len(A) and b <len(B):
        #         #비교후 추가
        #         if A[a] < B[b]:
        #             ans.append(A[a])
        #             a+=1
        #         else :
        #             ans.append(B[b])
        #             b+=1
        #     #둘 중 하나가 끝까지 갔을 때
        #     if a<len(A):
        #         ans.extend(A[a:])
        #     else:
        #         ans.extend(B[b:])
            
        #     return ans
        
        # return(merge(A,B))

        # 3. two pointers
        ans = collections.deque()
        l,r = 0, len(nums) - 1
        
        while l<=r:
            left, right = abs(nums[l]), abs(nums[r])

            if left > right:
                ans.appendleft(left**2)
                l+=1
            else:
                ans.appendleft(right**2)
                r-=1
        return list(ans)