#地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。
#一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下
#移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和
#大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，
#因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。
#请问该机器人能够到达多少个格子？

#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof


def digitsum(n):
    ans = 0
    while n:
        ans += n % 10
        n = n // 10
    return ans

class Solution:
    def movingCount(self, m: int, n: int, k :int) -> int:
        vis = set([(0,0)])
        for i in range(m):
            for j in range(n):
                if ((i-1, j) in vis or (i, j-1) in vis) and digitsum(i)+digitsum(j) <= k:
                    vis.add((i,j))
        return len(vis)