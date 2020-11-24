# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        ind = inorder.index(preorder[0])
        root = TreeNode(preorder[0])
        left = self.buildTree(preorder[1:ind+1], inorder[:ind] ) # ind��ʾ�������ж��ٸ�Ԫ�أ����������Ǵ�1��ind+1
        right = self.buildTree(preorder[ind+1:], inorder[ind+1:]) # ���������� root���Ԫ��
        root.left = left
        root.right = right

        return root
