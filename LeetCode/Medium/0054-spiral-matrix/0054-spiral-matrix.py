from collections import deque

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        # [1,2,3],
        # [4,5,6],
        # [7,8,9]

        res = []
        
        # pop(0) 작업 -> deque 로 관리
        matrix_deque = deque(deque(row) for row in matrix)

        while matrix_deque:

        # add first row - matrix.pop
            top = matrix_deque.popleft()
            res.extend(top)

        # down -> row[::-1] pop

            for row in matrix_deque:
                if row:
                    right = row.pop()
                    res.append(right)

        # add last row -> reverse
            if matrix_deque:
                bottom = matrix_deque.pop()
                res.extend(reversed(bottom))

        # up -> row[0] pop
            for row in reversed(matrix_deque):
                if row:
                    left = row.popleft()
                    res.append(left)
    
        return res
