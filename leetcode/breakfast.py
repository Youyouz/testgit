#С���������м�ѡ����һ�����̯λ��һά�������� staple �м�¼��ÿ����ʳ�ļ۸�
#һά�������� drinks �м�¼��ÿ�����ϵļ۸�С�۵ļƻ�ѡ��һ����ʳ��һ�����ϣ�
#�һ��Ѳ����� x Ԫ���뷵��С�۹��ж����ֹ��򷽰���

#ע�⣺����Ҫ�� 1e9 + 7 (1000000007) Ϊ��ȡģ���磺�����ʼ���Ϊ��1000000008��
#�뷵�� 1

#��Դ�����ۣ�LeetCode��
#���ӣ�https://leetcode-cn.com/problems/2vYnGI

class Solution:
    def breakfastNumber(self, staple: List[int], drinks: List[int], x: int) -> int:
        staple.sort()
        drinks.sort()
        m, n = len(staple), len(drinks)
        nums, i, j = 0, 0, n - 1
        while i < m and j >= 0:
            if staple[i] + drinks[j] <= x: 
                nums += j + 1
                i += 1
            else:
                j -= 1
        return nums % 1000000007