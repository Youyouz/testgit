#�� n �����򣬱��Ϊ0 �� n-1��ÿ�������϶�����һ�����֣���Щ���ִ�������?nums?�С�

#����Ҫ����������е����������������� i ���Ϳ��Ի��?nums[left] * nums[i] * nums[right]?��Ӳ�ҡ�?
#�����?left?��?right?�����?i?���ڵ������������š�ע�⵱����������� i ������?left?������?right?�ͱ�������ڵ�����

#�����ܻ��Ӳ�ҵ����������

#��Դ�����ۣ�LeetCode��
#���ӣ�https://leetcode-cn.com/problems/burst-balloons

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        val = [1] + nums + [1]
        @lru_cache(None)
        def solve(left:int, right:int) -> int:
            if left >= right-1:
                return 0
            
            best = 0
            for i in range(left+1, right):
                total = val[left] * val[i] * val[right]
                total += solve(left, i) + solve(i, right)
                best = max(best, total)
            return best

        return solve(0, n+1)