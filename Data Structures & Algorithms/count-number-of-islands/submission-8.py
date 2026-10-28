class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):
            q = deque()
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            q.append((r, c))
            visited.add((r, c))

            
            while q: 
                row, col = q.popleft()

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc 
                    if (nr >= 0 and nr < ROWS and nc >= 0 and nc < COLS and 
                    (nr, nc) not in visited and
                    grid[nr][nc] == "1"):
                        q.append((nr, nc))
                        visited.add((nr, nc))
                   


        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands +=1 
        return islands

