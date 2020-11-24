
#输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
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
        left = self.buildTree(preorder[1:ind+1], inorder[:ind] ) # ind表示左子树有多少个元素，所以这里是从1到ind+1
        right = self.buildTree(preorder[ind+1:], inorder[ind+1:]) # 这里填充的是 root这个元素
        root.left = left
        root.right = right

        return root
