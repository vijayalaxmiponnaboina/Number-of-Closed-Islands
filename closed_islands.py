from collections import deque
class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        q=deque()
        ans=0
        visited=[[False]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0 and not visited[i][j]:
                    q.append((i,j))
                    visited[i][j]=True
                    isclosed=True
                    while q:
                        size=len(q)
                        for x in range(size):
                            r,c=q.popleft()
                            if r==0 or r==m-1 or c==0 or c==n-1:
                                isclosed=False
                            if r-1>=0 and grid[r-1][c]==0 and  not visited[r-1][c]:
                                q.append((r-1,c))
                                visited[r-1][c]=True

                            if r+1<m and grid[r+1][c]==0 and  not visited[r+1][c]:
                                q.append((r+1,c))
                                visited[r+1][c]=True

                            if c-1>=0 and grid[r][c-1]==0 and  not visited[r][c-1]:
                                q.append((r,c-1))
                                visited[r][c-1]=True

                            if c+1<n and grid[r][c+1]==0 and  not visited[r][c+1]:
                                q.append((r,c+1))
                                visited[r][c+1]=True
                    if isclosed:
                                    ans+=1
        return ans
                                