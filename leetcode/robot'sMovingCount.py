#������һ��m��n�еķ��񣬴����� [0,0] ������ [m-1,n-1] ��
#һ�������˴����� [0, 0] �ĸ��ӿ�ʼ�ƶ�����ÿ�ο��������ҡ��ϡ���
#�ƶ�һ�񣨲����ƶ��������⣩��Ҳ���ܽ�������������������λ֮��
#����k�ĸ��ӡ����磬��kΪ18ʱ���������ܹ����뷽�� [35, 37] ��
#��Ϊ3+5+3+7=18���������ܽ��뷽�� [35, 38]����Ϊ3+5+3+8=19��
#���ʸû������ܹ�������ٸ����ӣ�

#��Դ�����ۣ�LeetCode��
#���ӣ�https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof


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