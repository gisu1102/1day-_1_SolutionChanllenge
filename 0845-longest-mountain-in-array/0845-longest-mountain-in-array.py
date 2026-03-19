class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        # arr = [2,1,4,7,3,2,5]
        # res = 5 / 1 4 7 3 2

        res = 0
        up = 0
        down = 0

        for idx in range(1, len(arr)):

            #up -> ++
            #if up > 0 , down-> down++
            # idx ++ 넘어갈때 마다 최대강 갱신
            # 

            if (down > 0 and arr[idx] > arr[idx - 1]) or arr[idx] == arr[idx - 1]:
                    up=0
                    down=0

            if arr[idx] > arr[idx-1]:
                up += 1
            elif (up>0) and (arr[idx]<arr[idx-1]):
                down += 1
            if(up>0) and (down>0):
                res = max(res,up+down+1)
        return res

            # up -> ++, down --
            # 1 2 3 2 4
            
            # 1 4 , up ++
            # 4 7 , up ++
            # 7 3 , down -- #초기화후 계산
            # 3 2 , down --
            # 계산
            # -> cnt == 0 
            # -> continue