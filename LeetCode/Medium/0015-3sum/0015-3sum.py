class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        #3개의 합 = 0 이되는 모든 경우의수
        # nums = [-1,0,1,2,-1,-4]
        
        sorted_nums = sorted(nums)
        #sorted_nums = [-4 -1 -1 0 1 2]
        #               i.  j->move  k
        #i=0 부터 j-2
        #j=1 부터 k-1
        #k=n 부터 j+1

        res = []

        # idx -> seq 순회
        for idx , num in enumerate(sorted_nums):
            #-1 -1 0 1 2
                # -1 -1 2 /-1 -1 1 / -1 0 1 
            #   -1 0 1 2
                # -1 0 2 / -1 0 1

            #idx가 prev 와 같으면 pass
            if (idx>0) and (num == sorted_nums[idx-1]):
                continue

            if num > 0:
                break

            left = idx+1
            right = len(sorted_nums)-1

            #left == right stop
            while left < right:
                left_num = sorted_nums[left]
                right_num = sorted_nums[right]
                #현재합 계산
                current_sum = num + left_num + right_num
                
                if current_sum > 0:
                    right -= 1
                elif current_sum < 0:
                    left +=1
                else: #정답을 찾은경우
                    res.append([num, left_num, right_num])
                    left += 1
                    right -= 1

                    while left < right and sorted_nums[left] == sorted_nums[left - 1]:
                        left += 1
                    while left < right and sorted_nums[right] == sorted_nums[right + 1]:
                        right -= 1    
        return res




        