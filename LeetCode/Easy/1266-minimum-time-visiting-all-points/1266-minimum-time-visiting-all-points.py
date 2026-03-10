class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        
        res = 0

        #[1,1],[3,4],[-1,0]
        #[1,1],[3,4] -> 3
        # 2, 3 (1,1)*2 up*1

        x1, y1 = points.pop() #1,1
        while points:
            x2, y2 = points.pop() #3,4

            diff = max(abs(y2-y1), abs(x2-x1))
            res += diff

            x1, y1 = x2, y2 # 3,4
        
        return res
