"""
    从二叉搜索树到更大和树
    ~~~~~~~~~~~~~~~~~~
    给出二叉 搜索 树的根节点，该二叉树的节点值各不相同，修改二叉树，
    使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。

    提醒一下，二叉搜索树满足下列约束条件：

        节点的左子树仅包含键 小于 节点键的节点。
        节点的右子树仅包含键 大于 节点键的节点。
        左右子树也必须是二叉搜索树。

    示例：
        输入：[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
        输出：[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
"""

"""
    解题思路：
        反向中序遍历 累加
        
"""
from typing import Union
from typing import NoReturn

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    sum = 0

    def bstToGst(self, root: TreeNode) -> Union[TreeNode, NoReturn]:
        if not root:
            return

        self.bstToGst(root.right)
        self.sum += root.val
        root.val = self.sum
        self.bstToGst(root.left)
        return root
