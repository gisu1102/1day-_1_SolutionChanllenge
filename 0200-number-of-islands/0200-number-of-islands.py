from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # 섬의 시작점 -> 연결된 모든 점을 찾아서 카운트
        #bfs
        # 0 0
        # 01 10
        #    10 02 11
        #       02 11 20 ,,,
        # 더 이상 방문 불가 -> fin
        # 다음 1을 찾아서,,

        # 1-> count ++ bfs/dfs 로 섬 전체 지우기
        # 시작점 = 1
        # 방문처리 = 1 만나자마자
        # 이동방향= 상하좌우
        # 종료조건 = 0, 더이상 이동불가

        count = 0
        rows, columns = len(grid), len(grid[0])
        directions = ((1, 0), (-1, 0), (0, -1), (0, 1)) #상하좌우

        def bfs(sr, sc):
            queue = deque()
            queue.append((sr,sc))
            grid[sr][sc] = -1

            while queue:
                r,c = queue.popleft()
                for dr,dc in directions:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < rows and 0 <= nc < columns:
                        if grid[nr][nc]=='1':
                            grid[nr][nc] = -1
                            queue.append((nr,nc))

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == '1':
                    count += 1
                    bfs(r,c)
        return count








        #-----------------------#

        # count = 0
        # rows, columns = len(grid), len(grid[0])
        # visited = set()
        # directions = [[1,0], [-1,0], [0,-1], [0,1]] #상하좌우

        # def bfs(sr, sc):
        #     queue = deque()
        #     queue.append((sr,sc))
        #     visited.add((sr,sc))

        #     while queue:
        #         r,c = queue.popleft()
        #         for dr,dc in directions:
        #             nr, nc = dr + r, dc + c
        #             if nr in range (rows) and nc in range (columns):
        #                 if grid[nr][nc]=='1' and (nr,nc) not in visited:
        #                     visited.add((nr,nc))
        #                     queue.append((nr,nc))

        # for r in range(rows):
        #     for c in range(columns):
        #         if grid[r][c] == '1' and (r,c) not in visited:
        #             count += 1
        #             bfs(r,c)
        # return count





        