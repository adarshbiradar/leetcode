class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        temp = sum(sum(x) for x in grid)
        ltor =[max(x) for x in grid]
        ttob = []
        for i in range(len(grid)):
            ttob.append(max(li[i] for li in grid))

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                grid[i][j] = min(ltor[i],ttob[j])

        result = sum(sum(x) for x in grid)

        return result-temp
