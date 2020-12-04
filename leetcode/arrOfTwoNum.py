#��������?�ǿ� ������������ʾ�����Ǹ������������У����Ǹ��Ե�λ���ǰ���?
#����?�ķ�ʽ�洢�ģ��������ǵ�ÿ���ڵ�ֻ�ܴ洢?һλ?���֡�

#��������ǽ��������������������᷵��һ���µ���������ʾ���ǵĺ͡�

#�����Լ���������� 0 ֮�⣬���������������� 0?��ͷ��

#��Դ�����ۣ�LeetCode��
#���ӣ�https://leetcode-cn.com/problems/add-two-numbers
#���룺(2 -> 4 -> 3) + (5 -> 6 -> 4)
#�����7 -> 0 -> 8
#ԭ��342 + 465 = 807

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = p = ListNode(None)
        s = 0
        while l1 or l2 or s:
            s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            p.next = ListNode(s % 10)
            p = p.next
            s //= 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next