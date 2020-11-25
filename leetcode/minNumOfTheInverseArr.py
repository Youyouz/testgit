#��һ�������ʼ�����ɸ�Ԫ�ذᵽ�����ĩβ�����ǳ�֮Ϊ�������ת��
#����һ����������������һ����ת�������ת�������СԪ�ء�
#���磬����?[3,4,5,1,2] Ϊ [1,2,3,4,5] ��һ����ת�����������СֵΪ1��

#��Դ�����ۣ�LeetCode��
#���ӣ�https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        lens = len(numbers)
        left, right = 0, lens-1
        while left < right:
            mid = (left + right) // 2
            if numbers[mid] > numbers[right]:
                left = mid + 1
            elif numbers[mid] == numbers[right]:
                right -= 1
            else:
                right = mid
        return numbers[left]